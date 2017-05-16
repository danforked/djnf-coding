import os
import csv
import statistics
import tweepy

# set up twitter client
consumer_key = os.environ.get('djnf_tw_consumer_key', None)
consumer_secret = os.environ.get('djnf_tw_consumer_secret', None)
access_token = os.environ.get('djnf_tw_token', None)
access_token_secret = os.environ.get('djnf_tw_token_secret', None)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# spin thru MLB data, find descriptive statistics
with open('data/mlb.csv', 'r') as f:
    reader = csv.DictReader(f)
    salaries = [float(row['SALARY']) for row in reader]
    count = len(salaries)
    total = "${:,}".format(int(sum(salaries)))
    average = "${:,}".format(int(statistics.mean(salaries)))
    median = "${:,}".format(int(statistics.median(salaries)))

    thing_to_tweet = 'MLB opening day 2016 stats:\n- Players: {}\n' \
                     '- Total payroll: {}\n- Average: {}\n' \
                     '- Median: {}'.format(count, total, average, median)

    api.update_status(status=thing_to_tweet)
