import tweepy
#import twitter_credentials
import time
print("from my twitter bot")
CONSUMER_KEY='wBC2fVnpIZoPE2myzhSTYRrG2'
CONSUMER_SECRET='sPLwdInp850CD8jDHKcEJAH4AkK2cORUb0YtCC8GugQYpbGy0x'
ACCESS_KEY='2999036906-AbewsOp0vg8esC99EmRn7L9pNGsRDEKChCz6qXh'
ACCESS_SECRET='pHxRmWVfRRxhUxXjfcpj02eYepLsmIaHkPi1jnRhWg5SK'
auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api=tweepy.API(auth)

FILE_NAME='last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read=open(file_name, 'r')
    last_seen_id=int(f_read.read().strip())
    f_read.close()
    return(last_seen_id)

def store_last_seen_id(last_seen_id, file_name):
    f_write=open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


#+mention.user.screen_name
def reply_to_tweets():
         print("Replying and revoking...")
         last_seen_id=retrieve_last_seen_id(FILE_NAME)
         mentions=api.mentions_timeline(last_seen_id,
                                  tweet_mode='extended')
         for mention in reversed(mentions):
                 print(str(mention.id)+"-"+mention.full_text)
                 last_seen_id=mention.id
                 store_last_seen_id(last_seen_id, FILE_NAME)
                 if '#helloworld' in mention.full_text.lower():
                       print("hello to uuu response back from the bot ")
                       api.update_status('@'+mention.user.screen_name+'hello world back to u and this is just a test', mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)
