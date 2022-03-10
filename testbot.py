import tweepy
import unittest
import bot
import os

class TestBot(unittest.TestCase):

    def setUp(self):
        self.api_key = os.environ.get("API_KEY")
        self.api_secret_key = os.environ.get("API_KEY_SECRET")
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        self.auth = tweepy.OAuth1UserHandler(self.api_key, self.api_secret_key, 
        self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def test_getAPIKeys(self):
        """ getAPIKeys should return both api_key and api_secret_key 
            from the environment variable
        """    
        result, res = bot.getAPIkeys()
        self.assertTupleEqual((result,res), (self.api_key, self.api_secret_key))

    def test_getAccess(self):
        """ getAccess should return a granted access token"""
        result = bot.getAccess(self.api_key, self.api_secret_key)
        self.assertIsInstance(result, type(self.api))
    
    def test_getEndpoint(self):
        """ getEndpoint should return an endpoint that can 
            generate a token.
        """
        result = bot.getEndpoint(self.api_key, self.api_secret_key)
        self.assertTrue(bool(result))

if __name__ == '__main__':
    unittest.main()    
