import tweepy

from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'yourapikey'

client = swagger.ApiClient(apiKey, apiUrl)

class TwitterAPI:
    def __init__(self):
        consumer_key = "yourkey"
        consumer_secret = "yoursecret"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "yourtoken"

        access_token_secret = "yourtokensecret"

        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

wordApi = WordApi.WordApi(client)
definitions = wordApi.getDefinitions('word',
                                     partOfSpeech='noun',
                                     sourceDictionaries='wordnet',
                                     limit=1)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("%s:\n%s" % (definitions[0].word, definitions[0].text))
