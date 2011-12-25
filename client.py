import tweepy

class TwitterClient(object):
    """
        A Tweeter client that implements the basic operations
    """

    def __init__(self, settings):

        auth = tweepy.OAuthHandler(settings["TWITTER_CONSUMER_KEY"], settings["TWITTER_CONSUMER_SECRET"])
        auth.set_access_token(settings["ACCESS_KEY"], settings["ACCESS_SECRET"])
        self.api = tweepy.API(auth)        

    def post(self, tweet):
        self.api.update_status(tweet)

    def get_friends_tweets(self):
        return self.api.friends_timeline()

    def get_friends(self, name=''):
        return self._get_filtered(self.api.friends(), 'name', name)

    def get_friend(self, name=''):
        return self.get_friends(name)[0]

    def get_trends(self, name=''):
        return self.api.trends()

    def _get_filtered(self, collection, key, value):
        return [o for o in collection if value in o.__dict__.get(key, '')]

    def get_my_tweets(self):
        return self.api.user_timeline()
