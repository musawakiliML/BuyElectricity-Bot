from app.server.utils.vtpass import VTPASS, VTPASSCredentials

from app.server.config.config import Settings
from uuid6 import uuid7
from datetime import datetime

settings = Settings()

api_key = settings.VTPASS_API_KEY
public_key = settings.VTPASS_PUBLIC_KEY
secret_key = settings.VTPASS_SECRET_KEY

vtpass_credentials = VTPASSCredentials(api_key, public_key, secret_key, is_live=False)

credentials = vtpass_credentials.credentials()

vtpass = VTPASS()

def generated_request_id():
    date_time_id = datetime.now().strftime('%Y%m%d%H%M')
    reference_id = str(uuid7()).split("-")[4]
    return date_time_id + reference_id