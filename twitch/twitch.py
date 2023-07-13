import os
import json
import requests
from dotenv import load_dotenv
import sys

sys.path.insert(1, '../')
from setup import setup

load_dotenv
url = 'https://api.twitch.tv/helix/eventsub/subscriptions'
client_id = setup.CLIENT_ID
client_secret = setup.CLIENT_SECRET

def getAccessToken():
    access_token = setup.ACCESS_TOKEN
    authValidation = validateAuthentication(access_token=access_token)
    if authValidation:
        return access_token
    return generateAccessToken()
    
def generateAccessToken():
    auth_body = {
        "client_id" : client_id,
        "client_secret" : client_secret,
        "grant_type" : "client_credentials",
    }
    auth_response = requests.post("https://id.twitch.tv/oauth2/token", auth_body)

    auth_response_json = auth_response.json()
    os.environ["ACCESS_TOKEN"] = auth_response_json['access_token']
    return os.environ.get("ACCESS_TOKEN")


def getHeaders():
    headers = {
        "Client-ID" : client_id,
        "Authorization": f"Bearer {getAccessToken()}"
    }
    return headers

def getUserID():
    url = "https://api.twitch.tv/helix/users"
    params = {
        "login":setup.USER_LOGIN
    }
    response = requests.get(url=url, headers=getHeaders(), params=params)
    response_json = response.json()
    try:
        return response_json['data'][0]['id']
    except:
        return "Error retrieving ID"
    
def validateAuthentication(access_token):
    validateHeaders = {
        "Authorization": f"Bearer {access_token}"
    }
    try:
        response = requests.get(url="https://id.witch.oauth2/validate", headers=validateHeaders)
        response_json = response.json
        return response.status_code == requests.codes.ok and response_json['client_id'] == client_id
    except:
        return False