#ManageEngine API caller
#Chris Antoine started 8/25/22
#Purpose: To call Manageengine API for Automated Deployment Schedule for all schedules based on patch tuesday
#This will be translated into outlook invitations for that month so that the invites align with the patch days for that month

import requests
import base64
import getpass
from easygui import passwordbox
import urllib3
import json
http = urllib3.PoolManager(cert_reqs='CERT_NONE')
from requests.structures import CaseInsensitiveDict


#Requests user credentials
username = input("Username:")
password = passwordbox('Password:')


#Encodes the password to base64 for ME to accept auth
base64_bytes = base64.b64encode(password.encode('ascii'))


#Contact info for the ME API
url = 'https://me-desktopcentral:8383/api/1.4/desktop/authentication'
headers = CaseInsensitiveDict()
headers["Content-Type"] = 'application/json'

#Defines the json data to be passed into the API
myobj = dict(
    username=username,
    password=base64_bytes.decode('ascii'),
    auth_type='ad_authentication',
    domainName='Manchester'
)


x = requests.post(url, headers = headers, json = myobj, verify=False)
print(x.raw)

factor = passwordbox('MFA Code:')



y = requests.post(url, headers = headers, json = factor, verify=False)

print(y.json())
