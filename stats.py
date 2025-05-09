def whats_the_word(file_contents):
	iso_words_list = file_contents.split()
	word_count = len(iso_words_list)
	return word_count



def character_counter(text):
	iso_characters = list(text.lower())
	dictionary = {}

	for char in iso_characters:
		if char.isalpha():
			if char in dictionary:
				dictionary[char] += 1
			else:
				dictionary[char] = 1
	return dictionary

	



def pretty(counts):
	## we want to return a sorted list of dictionaries such as..
	## each dictionary should have a key value pair as such {"char": "d", "num": 24}
	## sort the list from greates to least count
	## use the sort() method here as fit 
	
	#1. i want to assign the first key in the counts dictionary we are accepting to the value
	#    of the first key we are creating in a pre-defined dictionary ^
	
	list_pairs = []

	for key in counts:
		pair = {}
		pair["char"] = key
		pair["num"] = counts[key]
		list_pairs.append(pair)
	
	list_pairs.sort(key=lambda d: d["num"], reverse=True)
	
	output = ""
	
	for pair in list_pairs:
		output += f"{pair['char']}: {pair['num']}\n"
	return output.strip()
			
