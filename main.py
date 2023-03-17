from twython import Twython
import tweepy
import requests
import time
from datetime import datetime
import pandas as pd
import pytz
import logging
import logging.handlers

def msg(message):
    print(message)
    
    bot_token = '5041715929:AAFcraPI9-8jZR0bLkquRDNUXg96tEUKje4'
    bot_chatID = '1259144189'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='+ bot_chatID + '&parse_mode=MarkdownV2&text=' + message

    response = requests.get(send_text)
    print(response.json())
    return response.json()

try:
    CONSUMER_KEY = str(os.environ["CONSUMER_KEY"])
    CONSUMER_SECRET = str(os.environ["CONSUMER_SECRET"])
    ACCESS_TOKEN = str(os.environ["ACCESS_TOKEN"])
    ACCESS_TOKEN_SECRET = str(os.environ["ACCESS_TOKEN_SECRET"])
except KeyError:
    msg("Token not available!")
    #logger.info("Token not available!")
    #raise

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


# consumer_key = "Kk6YsDOoMrZ3dleewI5PyoFBG"
# consumer_secret = "SfNeq91UGvi7Se797iEflaOsuQ3M61nfJey04PTc3Oikz9FvBm"
# access_token = "1392839370843906050-hWAZNtev8MaisB2xdv3hPBQ7ybkm8r"
# access_token_secret = "ReY9BzjN82rHAApkuTi7j7cIYxv4YxVIYHimg6Gwd1jQ2"

start = 0
try:
    if start == 0:
        twitter = Twython(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
        )
        # authorization of consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        # set access to user's access key and access secret 
        auth.set_access_token(access_token, access_token_secret)
        
        # calling the api 
        api = tweepy.API(auth)
        
        # WOEID of London
        woeid_ind = 23424848
        
        # fetching the trends
        trends = api.trends_place(id = woeid_ind)
        
        # printing the information
        print("The top trends for the location are :")
        trendLst = []

        print("The top trends for the location are :")
        trendLst = []
        for value in trends:
            for trend in value['trends']:
                trendLst.append(trend['name'])
                now = datetime.now()
                current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
                print(current_time.date(),current_time.time(),trend['name'],trend['tweet_volume'])
                c_date = str(current_time.date())
                c_time = current_time.time()
                trending = trend['name']
                volume = trend['tweet_volume']

                logger.info(f'{c_date},{c_time},{trending},{volume}')
except Exception as e:
  
  msg("Process Stopped Need your attention")


