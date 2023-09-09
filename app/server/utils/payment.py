from app.server.utils.monnify_payment import MonnifyCredential, Monnify
from app.server.config.config import Settings
import uuid
import json

reserve = Monnify()
settings = Settings()

api_key = settings.MONNIFY_API_KEY
secret_key = settings.MONNIFY_SECRET_KEY
contractCode = settings.MONNIFY_CONTRACT_CODE
WalletAccountNo = settings.MONNIFY_WALLET_ACCOUNT_NO

merchant_credential = MonnifyCredential(
    api_key, secret_key, contractCode, WalletAccountNo, is_live=False)

token = merchant_credential.get_token()

def init_transaction(amount: float):
    
    paymentReference = str(uuid.uuid1())
    paymentReference = json.dumps(paymentReference, default=str)

    transaction = reserve.one_time_payment(credentials=merchant_credential.credentials(), amount=amount, customerName="EnergiEase Bot Customer", customerEmail="payment@energieasebot.ng", paymentReference=paymentReference, paymentDescription="Electricity Transaction", redirectUrl="", paymentMethods=["ACCOUNT_TRANSFER"])

    if transaction['responseMessage'] == "success":
        transactionReference = transaction['responseBody']['transactionReference']
        #print (transactionReference)
        return transactionReference

def init_bank_transfer(transactionReference: str):
    
    bank_transfer = reserve.pay_with_bank_transfer(credentials=merchant_credential.credentials(), transactionReference=transactionReference)
    if bank_transfer['responseMessage'] == "success":
        bank_details = {
            "Account Number": bank_transfer['responseBody']['accountNumber'],
            "Account Name": bank_transfer['responseBody']['accountName'],
            "Bank Name": bank_transfer['responseBody']['bankName'],
            "Amount": bank_transfer['responseBody']['amount']
        }
        return bank_details

def check_transaction_status(transactionReference: str) -> str:
    
    transaction_status = reserve.get_transaction_status(credentials=merchant_credential.credentials(),transactionReference=transactionReference, token=token)

    if transaction_status['responseMessage'] == "success":
        if transaction_status['responseBody']['paymentStatus'] == 'PAID':
            data = {
                "message":"Successfull"
            }
            return data
            #print(data)
        elif transaction_status['responseBody']['paymentStatus'] == 'PENDING':
            data = {
                "message": "Pending"
            }
            return data