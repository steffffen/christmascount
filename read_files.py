import os
import csv

file_dir = os.path.dirname(os.path.abspath(__file__))
speeches_dir = os.path.join(file_dir, 'speeches')


def get_speeches():
    speeches_dict = {}

    for speech in os.listdir(speeches_dir):
        speech_file = os.path.join(speeches_dir, speech)

        with open(speech_file, 'r') as speech_file_content:
            data = speech_file_content.read()\
            	.replace('\n', '')\
            	.replace(',', '')\
            	.replace('.', '')\
            	.replace('"', '')\
            	.replace("'", '')\
            	.replace(";", '')\
            	.replace("-", '')\
            	.replace(":", '')

            speeches_dict[speech] = data

    return speeches_dict


def write_list_to_csv(mylist, filename):

	csv_path = os.path.join(file_dir, filename)
	with open(csv_path, 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		for elm in mylist:
			wr.writerow([elm[0], elm[1]])


if __name__ == '__main__':
    get_speeches()
