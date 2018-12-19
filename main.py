import twitter
import datetime
import pytz
def cleaner_func(data, context):

     me = twitter.Api(consumer_key='XXXXXXXXXXXXXXXXX',
                         consumer_secret='XXXXXXXXXXX', 
                         access_token_key='XXXXXXXXXX', 
                         access_token_secret='XXXXXXX')

     tweets =  me.GetUserTimeline(count = 200)

     last_week = datetime.datetime.now() - datetime.timedelta(days=7)
     last_week = pytz.UTC.localize(last_week)

     i = 0
     for tweet in tweets:
          time =  datetime.datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y')
          if last_week > time:
               print('Deleting tweet: {}'.format(tweet.id))
               i += 1
               me.DestroyStatus(tweet.id)
     return 'deleted {} tweets'.format(i), 200
