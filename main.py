#ManageEngine API caller
#Chris Antoine started 8/25/22
#Purpose: To call Manageengine API for Automated Deployment Schedule for all schedules based on patch tuesday
#This will be translated into outlook invitations for that month so that the invites align with the patch days for that month

import requests
import base64
import getpass


#Requests user credentials
username = input("Username:")
password = input("Password:")


#Encodes the password to base64 for ME to accept auth
password_bytes = password.encode('ascii')
base64_bytes = base64.b64encode(password_bytes)
base64_password = base64_bytes.decode('ascii')


#Contacts the ME API
url = ('https://connect.gscu.org:8443/api/1.4/desktop/authentication')
myobj = {
    'username': username,
    'password': base64_password,
    'auth_type': 'ad_authentication',
    'domainName': 'Manchester'
    }

x = requests.post(url, json = myobj)
print(x)
