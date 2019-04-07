import time
from gpiozero import CamJamKitRobot
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

# your Twitter access codes go here
ckey = 'YOUR_CONSUMER_KEY_HERE'
csecret = 'YOUR_CONSUMER_SECRET_HERE'
atoken = 'YOUR_ACCESS_TOKEN_HERE'
asecret = 'YOUR_ACCESS_SECRET_HERE'

class listener(StreamListener):
    def on_data(self, data):
        blow()
        return True

bubbles = CamJamKitRobot()

def blow():
    bubbles.forward()
    time.sleep(8)
    bubbles.stop()

def blowshort():
    bubbles.forward()
    time.sleep(1)
    bubbles.stop()

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

blowshort()

twitterstream = Stream(auth, listener())
twitterstream.filter(track=['#blowbubbles'])
