import discord 
import tweepy
client = discord.Client() 

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
  if message.author != client.user:
      id = ""+str(message.channel)
      if id == "twitter":
        CK = "qQyf2BKpyh39YvR1VpVIOlEZS"
        CS = "kSGapIP5fK8Hjz23oOv9aOuVqUGiZT2lgTC3f7n2UF6j8DYc8k"
        auth = tweepy.OAuthHandler(CK,CS)
        AT = "1086013602262265861-rmxaTBsSTM157alrTYElh3JZHFm70N"
        AS = "0KAe1lDfA3ZB9BAuN4UdRXYTND8M6isEGDhNxaa7OyHSr"
        auth.set_access_token(AT,AS)
        api = tweepy.API(auth)
        api.update_status(message.content)

client.run('NTM1NjE5NTM1ODAyMzM1MjU0.DyK1nA.DxZ8IeqWta7qqjE8AmUo5z5smAk')