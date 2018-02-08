from syllable_finder import make_dictionary, return_syllable_count

''' 
Takes in a tweet and examines whether there is a haiku in the tweet or not.
The trump_haiku_list is an empty list that will be populated with a Haiku, in 
the form of a String, if a Haiku is found.
'''


def haiku_finder(tweet, trump_haiku_list):

	word_start = 0 # keeps track of the beginning of the possible haiku

	word_list = tweet.split() #split the word into a list of words

	syllable_dictionary = make_dictionary(word_list) # dictionary to reference

	while (word_list[word_start:]): # while the cut list is not empty

		current_word_list = word_list[word_start:] #increments start, cuts list
	
		word_start += 1

		line_1 = 0
		line_2 = 0
		line_3 = 0 #syllable counters for each line

		for word in current_word_list:


			if line_1 < 5:
				line_1 += syllable_dictionary[word]

				if line_1 > 5:
					break

			elif line_2 < 7:
				line_2 += syllable_dictionary[word]

				if line_2 > 7:
					break

			else:
				line_3 += syllable_dictionary[word]

				if line_3 == 5: 
					current_word = current_word_list.index(word) + 1
					haiku = current_word_list[word_start - 1:current_word]
					trump_haiku_list.append(haiku)

				if line_3 > 5:
					break

sentence = "Rasmussen just announced that my approval rating jumped to a far better number than I had in winning the Election, and higher than certain cows.” Other Trump polls are way up also. So why does the media refuse to write this? Oh well, someday!"

list = []

haiku_finder(sentence,list)

print(list)
