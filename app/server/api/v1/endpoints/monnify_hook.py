# Webhook For Transaction Nofication

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

import hashlib
import json
import hmac

from app.server.utils.verify_payment import verify_payment
from app.server.config.config import Settings

router = APIRouter()

settings = Settings()

monnify_secret_key = settings.MONNIFY_SECRET_KEY
monnify_ip = settings.MONNIFY_IP

# WebHook Validation

def verify_hash(payload_in_bytes, monnify_hash):
    """
    Recieves the monnify payload in bytes and perform a SHA-512 hash
    with your secret key which is also encoded in byte.
    uses hmac.compare_digest rather than "=" sign as the former helps
    to prevent timing attacks.
    """
    secret_key_bytes = monnify_secret_key.encode(
        "utf-8"
    )  # encodes your secret key as byte
    your_hash_in_bytes = hmac.new(
        secret_key_bytes, msg=payload_in_bytes, digestmod=hashlib.sha512
    )
    your_hash_in_hex = your_hash_in_bytes.hexdigest()  # Hexlify generated hash
    return hmac.compare_digest(your_hash_in_hex, monnify_hash)

def get_sender_ip(headers):
    """
    Get senders' IP address, by first checking if your API server
    is behind a proxy by checking for HTTP_X_FORWARDED_FOR
    if not gets sender actual IP address using REMOTE_ADDR
    """

    x_forwarded_for = headers.get("x-forwarded-for")
    if x_forwarded_for:
        # in some cases this might be in the second index ie [1]
        # depending on your hosting environment
        return x_forwarded_for.split(",")[0]
    else:
        return headers.get("remote-addr")

def verify_monnify_webhook(payload_in_bytes, monnify_hash, headers):
    """
    The interface that does the verification by calling necessary functions.
    Though everything has been tested to work well, but if you have issues
    with this function returning False, you can remove the get_sender_ip
    function to be sure that the verify_hash is working, then you can check
    what header contains the IP address.
    """

    return get_sender_ip(headers) == monnify_ip and verify_hash(
        payload_in_bytes, monnify_hash
    )

@router.post("/", status_code=status.HTTP_200_OK)
async def process_webhook(request: Request):
    """
    A function based view implementing the receipt of the webhook payload.
    The webhook payload should be received as bytes rather than json
    that would be converted to bytes.This is most likely one of the
    cause for failed webhook verification.
    After the webhook verification, you can get a json format of the byte
    object by simply calling json.loads(payload_in_bytes)
    """

   #  Headers({'host': 'living-optimal-seahorse.ngrok-free.app', 'user-agent': 'okhttp/3.12.2', 'content-length': '871', 'accept-encoding': 'gzip', 'apihost': 'https://living-optimal-seahorse.ngrok-free.app/monnifywebhook/', 'content-type': 'application/json;charset=UTF-8', 'monnify-signature': '4277c62ed3791f07efef0cc4ac14b87cb3b1307efbc3eb5ddd381897a34ae619fd5ee0ae1acdce68c2a0e7578bf37cb76f80a73ef9b72e98b80b9e072b7b9e79', 'x-forwarded-for': '35.242.133.146', 'x-forwarded-proto': 'https'})

    payload_in_bytes = await request.body()
   #  print(request.headers.get("monnify-signature"))
    monnify_hash = request.headers["monnify-signature"]
    confirmation = verify_monnify_webhook(payload_in_bytes, monnify_hash, request.headers)
    print(request.headers)

    if confirmation is False:
        return JSONResponse(
            content={"status": "failed", "msg": "Webhook does not appear to come from Monnify"},
            status_code=status.HTTP_400_BAD_REQUEST)
    else:
        """
        if payload verification is successful, you can perform your necessary task, but if your planned processing would take time, you should first return a 200 response and process your stuff in background.
        """
        
        transaction_details = json.loads(payload_in_bytes)
        #print(json.loads(payload_in_bytes))

        if transaction_details['eventType'] == "SUCCESSFUL_TRANSACTION":
            transaction_reference = transaction_details['eventData']['transactionReference']
            transaction_status = transaction_details['eventData']['paymentStatus']

            await verify_payment(transaction_reference, transaction_status)
        elif transaction_details['eventType'] == "REJECTED_PAYMENT":
            transaction_reference = transaction_details['eventData']['transactionReference']
            transaction_status = "FAILED"
            await verify_payment(transaction_reference, transaction_status)

        return JSONResponse(
            content={"status": "success", "msg": "Webhook received successfully"}, status_code=status.HTTP_200_OK)

