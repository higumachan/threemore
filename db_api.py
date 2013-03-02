#coding:utf-8

import tweepy
import pymongo

consumer_key = "V4b6CwecLkFEsg6xL4vVA"
consumer_secret = "L2lIR7KNNUDvyMBxAU66Nx5mFVeG4T9d8SeWAc4L9o"
access_token = "1227273721-BatkeQ4dabfiqbJsa14pzyWfvwY36cnKJHilmd0"
secret_token = "xzgW1WWIgUz4YGXjeqR8mZbDoJosFYKo9kQ9fNV60"

oauth = tweepy.OAuthHandler(consumer_key, consumer_secret);
oauth.set_access_token(access_token, secret_token);

api = tweepy.API(oauth);

db = pymongo.Connection().three

