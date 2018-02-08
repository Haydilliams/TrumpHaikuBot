import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup
from num2words import num2words

url = 'http://www.wordcalc.com/index.php'

# Simply returns the syllable count of the desired word

def return_syllable_count(words):

	# Try block converts any numbers into their word equivalent. NOTE.
	# This converts numbers to ordinal, which is usually incorrect, 
	# but left intentionally because it's hilarious
	try:
		words = num2words(int(words), to = 'ordinal')
	except ValueError:
		words = words

	# encodes the desired word(s) into the text field of the website
	post_data = urllib.parse.urlencode({'text': words})

	post_data = post_data.encode('ascii')

	connection = urllib.request.urlopen(url, post_data)
	response = connection.read()
	connection.close()

	soup = BeautifulSoup(response, 'html.parser')
	pretty_soup = soup.prettify() # readable HTML output

	# Regex looking for the HTML containing the syllable count
	pattern = re.compile('Syllable Count\s+<\/td>\s+<td>\s+\d')
	first_result = pattern.findall(pretty_soup) # Syllable count is at the end

	syllable_count = re.compile('\d').findall(first_result.pop())

	syllables = int(syllable_count.pop())

	return syllables if syllables != 0 else 1

# creates a dictionary of words with syllables as their values

def make_dictionary(word_list):

	syllable_dictionary = {}

	for word in word_list:

		if word not in syllable_dictionary:

			syllable_dictionary[word] = return_syllable_count(word)

	return syllable_dictionary



