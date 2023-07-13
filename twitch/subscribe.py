import requests
from twitch import twitch
import json
from setup import setup

url = 'https://api.twitch.tv/helix/eventsub/subscriptions'

def requestRewards():
    rewardID = getRewardID()
    payload = {
        "type": "channel.channel_points_custom_reward_redemption.add",
        "version": "1",
        "condition": {
            "broadcaster_user_id": {{twitch.getUserID}},
            "reward_id": {{rewardID}}
        },
        "transport": {
            "method": "webhook",
            "callback": "https://localhost:443/webhooks/callback",
            "secret": {{setup.CLIENT_SECRET}}
        }
    }
    headers = {
        "Authorization": f"Bearer {twitch.getAccessToken()}",
        "Client-Id": setup.CLIENT_ID,
    }
    response = requests.post(url= url, params=payload, headers=headers)
    return response

def getRewardID():
    rewards = requestRewards()
    for data in rewards['data']:
        if data['title'] == setup.REWARD_NAME:
                return data['id']
    return ""

def requestRewards():
    url = "https://api.twitch.tv/helix/channel_points/custom_rewards"
    params = {
        "broadcaster_id" : twitch.getUserID(),
    }
    headers = {
        "Authorization": f"Bearer {twitch.getAccessToken()}",
        "Client-Id": setup.CLIENT_ID,
    }
    response = requests.get(url=url, headers=headers, params=params)
    response_json = response.json()
    return response_json