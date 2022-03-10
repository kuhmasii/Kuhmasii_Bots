import re
import tweepy
import os

def getAPIkeys():
	""" Function returns API keys from environment variable """
	api_key = os.environ.get("API_KEY")
	api_secret_key = os.environ.get("API_KEY_SECRET")
	
	return api_key, api_secret_key

def getAccess(apikey, apisecretkey):
	""" Function returns access the token """
	access_token = os.environ.get('ACCESS_TOKEN')
	access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
	auth = tweepy.OAuth1UserHandler(apikey, apisecretkey)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	return api

def getEndpoint(apikey, apisecretkey):
	""" Function returns an endpoint that will connect to  
		the twitter's API App.
	"""
	# endpoint for webapps to use
	callback_uri = "oob" # https://kuhmasii/twitter/callback
	auth = tweepy.OAuth1UserHandler(apikey, apisecretkey, callback_uri)
	# getting the endpoint url
	redirect_url = auth.get_authorization_url()	
	return redirect_url

# def getAccesstoken(user_pin, apikey, apisecretkey):
# 	""" Function uses pin to access the token """
# 	callback_uri = "oob" # https://kuhmasii/twitter/callback
# 	auth = tweepy.OAuth1UserHandler(apikey, apisecretkey, callback_uri)
# 	access_token = auth.get_access_token(user_pin)
# 	return access_token 

