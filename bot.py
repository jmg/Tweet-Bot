import random
import time

from client import TwitterClient
from optparse import OptionParser

from settings import auth


class TweetBot(object):
    """
        A tweet-bot capable to tweet once or forever.
        If you choose the forever mode you need to specify the
        delay between tweets.
    """
    
    client = TwitterClient(auth)
    
    def get_tweets_list(self):
        """
            Read tweets from a file.
            WARNING! The tweets.txt file must contain one tweet per line.
        """
        
        with open("tweets.txt", "r") as f:
            return f.readlines()
        
    def tweet(self):
        """
            Just tweet once
        """
        
        tweets = self.get_tweets_list()
        random.shuffle(tweets)
        
        for tweet in tweets:
            try:
                self.client.post(tweet)
                return
            except:
                continue
                
        print "I need more tweets"
        
    def delayed_tweet(self, delay):
        """
            Tweet forever
        """
        
        while 1:
            self.tweet()
            time.sleep(int(delay) * 60)
            

def main():
    
    bot = TweetBot()
    
    parser = OptionParser()
    parser.add_option("-t", "--time", help="Specify the delay between tweets (In minutes)")

    (options, args) = parser.parse_args()
   
    if options.time is not None:        
        bot.delayed_tweet(options.time)        
    else:
        bot.tweet()  

        
if __name__ == '__main__':
    
    main()
              
    
