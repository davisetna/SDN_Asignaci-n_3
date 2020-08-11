import requests 
from pprint import pprint

r = requests.get('https://sandboxsdwan.cisco.com:8443/dataservice/device' , auth=('devnetuser','Cisco123!') , verify=False )

info = r.json()

aux = info['data']
for data in aux:
    print("\n")
    pprint('HOST-NAME: '+ data['host-name'])
    pprint('DEVICE-TYPE: '+ data['device-type'])
    pprint('STATUS: '+ data['status'])


