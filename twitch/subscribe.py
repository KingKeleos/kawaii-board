import requests
from twitch import twitch
from setup import setup

url = 'https://api.twitch.tv/helix/eventsub/subscriptions'
webhookURL = 'https://webhook.site/8c80a5ae-f6ff-466f-a324-df7eb7b4685e'
privateURL = 'https://192.168.0.107/webhooks/callback'

def requestRewards():
    rewardID = getRewardID()
    if rewardID == "":
        return
    payload = {
        "type": "channel.channel_points_custom_reward_redemption.add",
        "version": "1",
        "condition": {
            "broadcaster_user_id": twitch.getUserID(),
            "reward_id": rewardID
        },
        "transport": {
            "method": "webhook",
            "callback": setup.TUNNEL,
            "secret": setup.CLIENT_SECRET
        }
    }
    headers = {
        "Authorization": f"Bearer {twitch.getAccessToken()}",
        "Client-Id": setup.CLIENT_ID,
    }
    response = requests.post(url= url, json=payload, headers=headers)
    return response

def getRewardID():
    rewards = listRewards()
    for data in rewards['data']:
        if data['title'] == setup.REWARD_NAME:
                print(f"Found Reward {setup.REWARD_NAME} with id: {data['id']}")
                return data['id']
    return ""

def listRewards():
    url = "https://api.twitch.tv/helix/channel_points/custom_rewards"
    params = {
        "broadcaster_id" : twitch.getUserID(),
    }
    headers = {
        "Authorization": f"Bearer {setup.USER_ACCESS_TOKEN}",
        "Client-Id": setup.CLIENT_ID,
    }
    response = requests.get(url=url, headers=headers, params=params)
    response_json = response.json()
    return response_json