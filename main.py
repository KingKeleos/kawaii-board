from twitch import twitch, subscribe
from dotenv import load_dotenv
from kawaii_board import board
import multiprocessing as mp
import json
import threading
from webhook import webhook
from setup import setup

from flask import Flask, request, Response, jsonify

app = Flask(__name__)
@app.route('/', methods=['POST'])
def return_response():
    p = mp.Process(target=startBoard)
    p.start()
    body = request.data
    body_json = json.loads(body)
    header = body_json["challenge"]
    return jsonify(header), 200

@app.route('/authorization')
def return_authorization():
    accessToken = twitch.getAccessToken()
    gotToken = False
    if accessToken:
        gotToken = True
    return f"Token created: {gotToken}"

@app.route('/userID')
def return_userID():
    id = twitch.getUserID()
    return f"UserID: {id}"

@app.route('/rewardID')
def return_rewardID():
    response = subscribe.getRewardID()
    return f"Response: {response}"

def startApp():
    thread = threading.Thread(target=app.run(host='0.0.0.0', port='443'))
    thread.start()

def startBoard():
    thread = threading.Thread(target=board.kawaii_board())
    thread.start()

if __name__ == "__main__":
    load_dotenv()
    mp.freeze_support()
    print("starting tunnel for twitch api")
    setup.TUNNEL = webhook.createTunnel()
    server = mp.Process(target=startApp)
    server.start()
    print("after Server start:")
    #response = subscribe.requestRewards()
    #print(response.status_code)