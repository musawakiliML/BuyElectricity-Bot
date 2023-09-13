from app.server.utils.vtpass import VTPASS, VTPASSCredentials

from app.server.config.config import Settings

settings = Settings()

api_key = settings.VTPASS_API_KEY
public_key = settings.VTPASS_PUBLIC_KEY
secret_key = settings.VTPASS_SECRET_KEY

vtpass_credentials = VTPASSCredentials(api_key, public_key, secret_key, is_live=False)

credentials = vtpass_credentials.credentials()

vtpass = VTPASS()

# verify_meter = vtpass.verify_meter(1111111111111, "ikeja-electric", "prepaid",credentials)

# print(verify_meter)
# "ikeja-electric"
# "eko-electric"
# "kano-electric"
# "portharcourt-electric"
# "jos-electric"
# "ibadan-electric"
# "kaduna-electric"
# "abuja-electric"
# "enugu-electric"
# "benin-electric"