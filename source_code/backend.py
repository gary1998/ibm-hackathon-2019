# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import PersonalityInsightsV3, ToneAnalyzerV3, NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions
import json
import tweepy
import time

app = Flask(__name__)
CORS(app)

class DataStore():
    api = None
    friend=[]
    follower=[]
    userObj = None

data = DataStore()

@app.route('/')
def hello():
    return "Welcome to backend server - developed in Flask Python"

@app.route('/twitterLogin')
def loginFunc():
    if 'consKey' and 'consSec' and 'accessTok' and 'accessSec' in request.args:
        consumer_key = request.args['consKey']
        consumer_secret = request.args['consSec']
        access_token = request.args['accessTok']
        access_token_secret = request.args['accessSec']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        data.api = tweepy.API(auth, wait_on_rate_limit=True)
        data.userObj = data.api.me()
        for user in tweepy.Cursor(data.api.friends, screen_name=data.userObj.screen_name).items():
            data.friend.append(str(user.screen_name))
        for user in tweepy.Cursor(data.api.followers, screen_name=data.userObj.screen_name).items():
            data.follower.append(str(user.screen_name))    
        return jsonify(name=data.userObj.name, followersNameList=data.follower, friendsNameList=data.friend)

@app.route('/fetch')
def fetchFunc():
    if 'name' in request.args:
        ffname = request.args['name']
        tweetsData = ""
        tweets = data.api.user_timeline(screen_name=ffname, count=100, tweet_mode='extended')
        for info in tweets[:8]:
            tweetsData += info.full_text
        return jsonify(tweets=tweetsData)

@app.route('/fetchMe')
def fetchMyFunc():
    myname = data.userObj.screen_name
    tweetsData = ""
    tweets = data.api.user_timeline(screen_name=myname, count=100, tweet_mode='extended')
    for info in tweets[:8]:
        tweetsData += info.full_text
    return jsonify(tweets=tweetsData)

@app.route('/analyze')
def analyzeFunc():
    if 'data' in request.args:
        text = request.args['data']

        authenticatorNLU = IAMAuthenticator('rW0-13R2RqRbko3bNzOaz1E8toSIy2qH1019AWiHkMZ9')
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=authenticatorNLU
        )
        natural_language_understanding.set_service_url('https://gateway-lon.watsonplatform.net/natural-language-understanding/api')
        emotions = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions(document=True))
        ).get_result()

        authenticatorPI = IAMAuthenticator('uA6GpdKCXJyJCqJyhQEqwH9jSJxqlJhgYq7-uBBfPYL5')
        personality_insights = PersonalityInsightsV3(
            version='2017-10-13',
            authenticator=authenticatorPI
        )
        personality_insights.set_service_url('https://gateway-lon.watsonplatform.net/personality-insights/api')
        personality = personality_insights.profile(
            text.encode('utf-8'),
            'application/json'
        ).get_result()

        return jsonify(emotions=emotions, personality=personality)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)