import os


file_dir = os.path.dirname(os.path.abspath(__file__))
speeches_dir = os.path.join(file_dir, 'speeches')


def get_speeches():
    speeches_dict = {}

    for speech in os.listdir(speeches_dir):
        speech_file = os.path.join(speeches_dir, speech)

        with open(speech_file, 'r') as speech_file_content:
            data = speech_file_content.read().replace('\n', '')
            speeches_dict[speech] = data

    print(speeches_dict)
    return speeches_dict


if __name__ == '__main__':
    get_speeches()
