""" Examples for the wordAPI """

import inspect

from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'yourapikey'
client = swagger.ApiClient(apiKey, apiUrl)

"""searchngram( blank is a blank )
print "%s is a %s" % (word1, word2)"""

""" wordAPI object """
wordApi = WordApi.WordApi(client)

theWord = 'wild'
definitions = wordApi.getDefinitions(theWord,
                                     partOfSpeech='adjective',
                                     sourceDictionaries='wordnet',
                                     limit=2)

print "Word: %s" % definitions[0].word

pronounce = wordApi.getTextPronunciations( theWord )
print "\tPronuncitation for %s: %s" % (theWord, pronounce[0].raw.encode("utf-8"))

print "\tFirst definition: %s" % definitions[0].text
print "\tSecond definition: %s" % definitions[1].text
print "\tSource Dictionary One: %s" % definitions[0].sourceDictionary
print "\tPart of speech: %s" % definitions[0].partOfSpeech
"""print definitions[0].attributionUrl
print definitions[0].relatedWords
print definitions[0].textProns"""

example = wordApi.getTopExample(theWord)
"""print "Word: %s" % example.word"""
print "\tExample: %s" % example.text.encode("utf-8")
print "\tSource URL: %s" % example.url
print "\tSource Title: %s" % example.title
print "\tYear Published: %s" % example.year

phrase = wordApi.getPhrases( theWord )
print "\tIn a phrase: %s %s" % (phrase[0].gram1.encode("utf-8"), phrase[0].gram2.encode("utf-8"))

etym = wordApi.getEtymologies( theWord )
print "\tEtymology: %s" % etym[0][0]

print '\n'

relWord = wordApi.getRelatedWords(theWord, useCanonical = 'true', relationshipTypes = 'synonym')
print "\tWords with relationship type: %s" % relWord[0].relationshipType
"""print len(relWord)"""

for word in relWord[0].words:
	print "\t\t%s" % word

print '\n'

""" wordsAPI object """
wordsApi = WordsApi.WordsApi(client)

""" Word of the Day """
wod = wordsApi.getWordOfTheDay()
print "Word of the Day: %s" % wod.word

print "\n<<< Definitions >>>"
for wodDef in wod.definitions:
	print "\t* %s" % wodDef.text.encode("utf-8")

print "\n<<< Examples >>>"
for ex in wod.examples:
	print "\tExample: %s" % ex.text.encode("utf-8")
	print "\t\tTitle: %s" % ex.title
	print "\t\tSource URL: %s\n" % ex.url
"""
wordListApi = WordListApi.WordListApi(client)
mylist = wordListApi.getWordListWords('tiger')

print mylist[0].word


print '\n'
print '\n'

members = inspect.getmembers(relateWord)
aMember = inspect.getmembers(relateWord[0])

for key, value in enumerate(relateWord):
	print key, value

for index in enumerate(members):
	print index

print '\n'

for index2 in enumerate(aMember[0]):
	print index2"""
