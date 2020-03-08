import requests 
from pprint import pprint

response = requests.post('https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token', auth=('devnetuser','Cisco123!'))
payload=response.json()
pprint(payload)









response.raise_for_status(),
response = requests.get(
	'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
	headers={'X-Auth-Token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ZTNkNDI5ZTdjZDQ3ZTAwNGM2N2RkMGMiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTU4MzYzNTEyMSwidXNlcm5hbWUiOiJkZXZuZXR1c2VyIn0.H9TFeQE47-95macIAdF-EMTk4Lriv2XhT-PEngcoAkI'})
api = response.json()
pprint(api)
