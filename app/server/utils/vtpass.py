# VTPASS Connection for Buying Electricity

import requests
import json

# API Base urls for testing and live production

class GetBaseUrl:
   def __init__(self, live):
       self.live = live
   def urls(self):
        if self.live == True:
            return 'https://api-service.vtpass.com/api'
        elif self.live == False:
            return 'https://sandbox.vtpass.com/api'
        else:
            # print(self.live)
            return 'live can either be True or False'

# Functions to Perform operations on VTPASS

class VTPASSCredentials:
   def __init__(self, api_key, public_key, secret_key, is_live):
      self.api_key = api_key
      self.public_key = public_key
      self.secret_key = secret_key
      self.is_live = is_live
   
   def credentials(self):
      data = (self.api_key, self.public_key, self.secret_key, self.is_live)
      return data

class VTPASS:
   
   def __init__(self) -> None:
      pass
   
   def get_balance(self, credentials):
      live = credentials[3]
      if live == True or live == False:
         baseurl = GetBaseUrl(live).urls()
         url = f"{baseurl}/balance"
         payload = {}
         headers = {
                'api-key': credentials[0],
                'public-key': credentials[1],
                'Content-Type': 'application/json'
            }
         response = requests.request('GET', url, headers=headers, data=json.dumps(payload))
         response_dict = json.loads(response.text)
         return response_dict
   
   def verify_meter(self, billersCode, serviceID, meter_type, credentials):
      live = credentials[3]
      if live == True or live == False:
         baseurl = GetBaseUrl(live).urls()
         url = f"{baseurl}/merchant-verify"
         payload = {
            "billersCode":billersCode,
            "serviceID":serviceID,
            "type":meter_type
         }
         headers = {
                'api-key': credentials[0],
                'secret-key': credentials[2],
                'Content-Type': 'application/json'
            }
         response = requests.request('POST', url, headers=headers, data=json.dumps(payload))

         response_dict = json.loads(response.text)
         return response_dict

   def purchase_electricity_unit(self, request_id: str, serviceID: str, billersCode: str, variation_code: str, amount: int, phone, credentials):
      live = credentials[3]
      if live == True or live == False:
         baseurl = GetBaseUrl(live).urls()
         url = f"{baseurl}/pay"
         payload = {
            "request_id":request_id,
            "serviceID":serviceID,
            "billersCode":billersCode,
            "variation_code":variation_code,
            "amount":amount,
            "phone":phone
         }
         headers = {
                'api-key': credentials[0],
                'secret-key': credentials[2],
                'Content-Type': 'application/json'
            }
         response = requests.request('POST', url, headers=headers, data=json.dumps(payload))

         response_dict = json.loads(response.text)
         return response_dict

   def transaction_status(self, request_id, credentials):
      live = credentials[3]
      if live == True or live == False:
         baseurl = GetBaseUrl(live).urls()
         url = f"{baseurl}/requery"
         payload = {
            "request_id":request_id
         }
         headers = {
                'api-key': credentials[0],
                'secret-key': credentials[2],
                'Content-Type': 'application/json'
            }
         response = requests.request('POST', url, headers=headers, data=json.dumps(payload))

         response_dict = json.loads(response.text)
         return response_dict