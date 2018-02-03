#!/usr/bin/python
import praw
import re
from collections import deque
from time import sleep
from datetime import datetime
import time
import sys

start_time = datetime.now()

reddit = praw.Reddit('bot7')

subreddit = reddit.subreddit("all")

comment_cache = deque(maxlen=200)

username = "R10E"

blacklist_subs = ["r/neoliberal", "r/sbubby"]

kappa = [(re.compile("(^|[^A-Za-z0-9])[Rr][Ee]{3,}([^A-Za-z0-9]|$)"), reddit.subreddit("REEEEEEEEEE")),
         (re.compile("(^|[^A-Za-z0-9])[Mm][Oo][Nn][Kk][Aa][Ss]([^A-Za-z0-9]|$)"), reddit.subreddit("monkaS")),
         (re.compile("(^|[^A-Za-z0-9])([Vv][Oo][Hh][Ii][Yy][Oo]|[Kk]on[Cc]ha|[Tt]e[Hh]e[Pp][eo]lo|[Pp]un[Oo]ko)([^A-Za-z0-9]|$)"), reddit.subreddit("VoHiYo"))]

def check_condition(c, regexsub):
    regex = regexsub[0]
    sub = regexsub[1]
    if username == c.author.name or sub.display_name.lower() in c.subreddit_name_prefixed.lower():
        return False
    title = c.title
    text = c.selftext
    if re.findall(regex, title):
        return True
    return True if re.findall(regex, text) else False

def bot_action(c, s):
    print(c.title.encode('utf-8'))
    print(c.selftext.encode('utf-8'))
    if "monkaS" != s.display_name and c.subreddit_name_prefixed.lower() not in blacklist_subs:
        s.submit(title="[{}] {}".format(c.subreddit_name_prefixed, c.title), url="https://www.reddit.com" + c.permalink, resubmit=False)
    else:
        s.submit(title="[{}] {}".format(c.subreddit_name_prefixed, c.title), selftext="https://www.reddit.com" + c.permalink, resubmit=False)

start_time = time.time()
print "bot is running..."
running = True
i = 0
backoff = 8
while running:
    try:
        # Necessary to run on PythonAnywhere scheduler because the task is killed automatically after 12-13 hours.
        # This is done so we voluntarily kill the task, so we can start it up twice per day, fixed schedule.
        if time.time() - start_time > 43000:
            print("I'm gonna rest for a bit...")
            sys.exit(0)
        commentz = subreddit.new(limit=100)
        i = (i + 1) % 65536
        if i % 256 == 0:
            print i
        for comment in commentz:
            try:
                if comment.id in comment_cache:
                    break
                comment_cache.append(comment.id)
                for regexsub in kappa:
                    bot_condition_met = check_condition(comment, regexsub)
                    if bot_condition_met:
                        bot_action(comment, regexsub[1])
                        backoff = 8
            except Exception as e:
                print("[ERROR]:{}".format(e))
                print("sleeping in {} sec".format(backoff))
                sleep(backoff)
                if backoff < 1024:
                    backoff = backoff * 2
    except KeyboardInterrupt:
        running = False
    except Exception as e:
        print("[ERROR]:{}".format(e))
        print("sleeping in {} sec".format(backoff))
        sleep(backoff)
        if backoff < 1024:
            backoff = backoff * 2
