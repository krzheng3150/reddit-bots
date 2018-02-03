#!/usr/bin/python
import praw
import re
from collections import deque
from time import sleep
from datetime import datetime
import time
import sys

start_time = datetime.now()

reddit = praw.Reddit('bot8')

subreddit = reddit.subreddit("ArenaHS+AskHearthstone+CompetitiveHS+HSPulls+TheHearth+customhearthstone+hearthstone")

dest_subreddit = reddit.subreddit("hearthsone")

username = "hearthsan-bot"

comment_cache = deque(maxlen=200)

def check_condition(c):
    if username == c.author.name:
        return False
    #print('{} {} {} {}'.format(len(c.selftext), c.permalink, c.url, "hearthstone" in c.title.lower()))
    if len(c.selftext) == 0 and c.permalink not in c.url:
        return "hearthstone" in c.title.lower()
    return (c.title.lower().count("hearthstone") + c.selftext.lower().count("hearthstone")) >= 3

def bot_action(c):
    print(c.title.encode('utf-8'))
    print(c.selftext.encode('utf-8'))
    title_occurrences = [m.start() for m in re.finditer('[Hh][Ee][Aa][Rr][Tt][Hh][Ss][Tt][Oo][Nn][Ee]', c.title)]
    text_occurrences = [m.start() for m in re.finditer('[Hh][Ee][Aa][Rr][Tt][Hh][Ss][Tt][Oo][Nn][Ee]', c.selftext)]

    title_arr = []
    x = 0
    for y in title_occurrences:
        title_arr.append(c.title[x:y])
        title_arr.append('Hearthsone')
        x = y + 11 # length of 'Hearthstone'
    title_arr.append(c.title[x:])
    submit_title = ''.join(title_arr)

    if len(c.selftext) == 0:
        post = dest_subreddit.submit(title=submit_title, url=c.url, resubmit=False)
        post.reply("https://www.reddit.com" + c.permalink)
        return

    text_arr = []
    x = 0
    for y in text_occurrences:
        text_arr.append(c.selftext[x:y])
        text_arr.append('Hearthsone')
        x = y + 11 # length of 'Hearthstone'
    text_arr.append(c.selftext[x:])
    submit_text = ''.join(text_arr)

    post = dest_subreddit.submit(title=submit_title, selftext=submit_text, resubmit=False)
    post.reply("https://www.reddit.com" + c.permalink)

start_time = time.time()
print "bot is running..."
ref_time = start_time - 90
running = True
i = 0
backoff = 8
while running:
    try:
        # Necessary to run on PythonAnywhere scheduler because the task is killed automatically after 12-13 hours.
        # This is done so we voluntarily kill the task, so we can start it up twice per day, fixed schedule.
        if time.time() - start_time > 42000:
            print("I'm gonna rest for a bit...")
            sys.exit(0)
        commentz = subreddit.new(limit=2)
        i = (i + 1) % 65536
        if i % 256 == 0:
            print i
        for comment in commentz:
            if comment.created_utc <= ref_time:
                break
            ref_time = comment.created_utc + 1
            try:
                if check_condition(comment):
                    bot_action(comment)
                    backoff = 8
                    time.sleep(30)
            except Exception as e:
                print("[ERROR]:{}".format(e))
                print("sleeping in {} sec".format(backoff))
                sleep(backoff)
                if backoff < 1024:
                    backoff = backoff * 2
    except Exception as e:
        print("[ERROR]:{}".format(e))
        print("sleeping in {} sec".format(backoff))
        sleep(backoff)
        if backoff < 1024:
            backoff = backoff * 2
    except KeyboardInterrupt:
        running = False
