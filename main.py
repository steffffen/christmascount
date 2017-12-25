import pprint

from read_files import get_speeches

speeches_dict = get_speeches()

count_dict = {}

test_string = "friede sei Gott in der Höhe"

test_string_2 = "friede sei Gott in der Höhe und auf Erden"

test_string_list = [test_string, test_string_2]

def count_words_in_string(string):
	wordlist = string.split(' ')

	for word in wordlist:
		word = word.lower()
		if word in count_dict.keys():
			count_dict[word] += 1
		else:
			count_dict[word] = 1

def list_iterate(list):
	for item in list:
		count_words_in_string(item)

def count_all():
	for year in speeches_dict.keys():
		count_words_in_string(speeches_dict[year])


#list_iterate(test_string_list)
count_all()

#print(count_dict)

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

pprint.pprint(sortFreqDict(count_dict))