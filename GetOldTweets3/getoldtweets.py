# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# .setNear("America")
import datetime
from datetime import date
# import GetOldTweets3 as got
from manager.TweetCriteria import TweetCriteria
from manager.TweetManager import TweetManager
from tqdm import tqdm
import time
from absl import app, flags
import os

FLAGS = flags.FLAGS
flags.DEFINE_string("hashtag", None, "hashtag name")
flags.DEFINE_spaceseplist("start", "2020 1 1", "start date")
flags.mark_flag_as_required("hashtag")


def main(args):
    hashtag = FLAGS.hashtag
    y = int(FLAGS.start[0])
    m = int(FLAGS.start[1])
    d = int(FLAGS.start[2])
    start = date(y, m, d)
    if not os.path.isdir(f'./{hashtag}'):
        os.mkdir(f'./{hashtag}')

    while (start < date.today()):
        since = start
        until = since
        until += datetime.timedelta(days=1)
        print(since, until)

        tweetCriteria = TweetCriteria().setQuerySearch(f"#{hashtag}")\
            .setSince(str(since))\
            .setUntil(str(until))\
            .setLang("en")\
            .setEmoji("unicode")

        tweets = TweetManager().getTweets(tweetCriteria)

        with open(f'./{hashtag}/{hashtag}_{start.strftime("%Y%m%d")}.txt', 'w', encoding="utf-8") as f_out:
            for tweet in tqdm(tweets):
                # print(tweet.text)
                # print("-------------")
                f_out.write('' + str(tweet.id) + ' !@#$%^&* ' +
                            str(tweet.permalink) + ' !@#$%^&* ' +
                            str(tweet.username) + ' !@#$%^&* ' +
                            str(tweet.to) + ' !@#$%^&* ' +
                            str(tweet.text) + ' !@#$%^&* ' +
                            str(tweet.date.strftime('%d %B %Y')) + ' !@#$%^&* ' +
                            str(tweet.retweets) + ' !@#$%^&* ' +
                            str(tweet.favorites) + ' !@#$%^&* ' +
                            str(tweet.mentions) + ' !@#$%^&* ' +
                            str(tweet.hashtags) + ' !@#$%^&* ' +
                            str(tweet.geo) + '\n')

        start += datetime.timedelta(days=1)
        # time.sleep(15*60)


if __name__ == '__main__':
    app.run(main)
