# wordBot

This Twitterbot is built using Python and two APIs:

* [The Wordnik API](http://developer.wordnik.com/)
* [The Tweepy API](http://www.tweepy.org/)

wordBot.py contains Python code for a Twitterbot that tweets word definitions.  It can easily be modified to produce more complex tweets.

word.py contains examples for the Wordnik API used to retrieve information about words.

# Running the bot

First, sign up for the necessary keys to access the APIs and Twitter and add those keys to the Python scripts.

Next, simply open a terminal, navigate to the Python scripts, and type:

* `python wordBot.py` to run the bot.  It will tweet your word definition to the account attached to your key.
* `python word.py` to view the output of the Wordnik API examples.

# Scheduling the bot

To schedule the bot to execute regularly you can use [crontab](http://www.computerhope.com/unix/ucrontab.htm) on Linux/Unix or set up a [scheduled task](https://www.drupal.org/node/31506) in Windows.
