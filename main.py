# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from typing import Dict, List


def read_file_content(filename):
    # [assignment] Add your code here
    try:
        text_file = open(filename, "r")
        return text_file.read()
    except:
        text_file.close()


def count_words():
    text_list = []
    text_dict = {}
    text = read_file_content("./story.txt")
    for sentences in text.split():
        text_list.append(sentences)

    for words in text_list:
        text_dict[words] =text_list.count(words)

    print(f"\nDATA DICTIONARY = {text_dict}\n")

count_words()