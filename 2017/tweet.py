import tweepy
import os

consumer_key = os.environ.get('djnf_tw_consumer_key', None)
consumer_secret = os.environ.get('djnf_tw_consumer_secret', None)
access_token = os.environ.get('djnf_tw_token', None)
access_token_secret = os.environ.get('djnf_tw_token_secret', None)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(status='hello world')
