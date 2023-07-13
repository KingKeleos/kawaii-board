from twitch import twitch, subscribe
from dotenv import load_dotenv
from setup import setup
from kawaii_board import board
import multiprocessing as mp
import json
import threading

from flask import Flask, request, Response, jsonify

app = Flask(__name__)
@app.route('/webhooks/callback', methods=['POST'])
def return_response():
    subscribe.requestRewards()
    board = mp.Process(target=board.kawaii_board())
    board.start()
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


if __name__ == "__main__":
    load_dotenv()
    mp.freeze_support()
    app.run(host='0.0.0.0', port='443')