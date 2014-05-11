# utilize a file named on the command line
from sys import argv

script, filename = argv

# open the file named on the command line
def open_read_close(some_file):
    f = open(some_file)
    filetext = f.read()
    f.close()
    return filetext

# We want to make everything lowercase before we separate it in separate()
def make_lower(some_string):
    some_string = some_string.lower()
    return some_string

# separate words by white space
def separate(some_string):
    output = some_string.split()
    return output

# strip the words of punctuation
# you're not making a copy of this list. You're changing the original list #Liz2Lizz
def strip_punctuation(some_list):
    for i in range(len(some_list)):
        some_list[i] = some_list[i].strip(".,'!?\";")
    return some_list

# create a dictionary to store words (keys) and their counts (values)
# count how many times a word occurs in that file
def counts(some_list):
    count_dict = {}
    for each in some_list:
        # if key is not in dictionary, create a new key and set it's value to 1
        if count_dict.get(each, 0) == 0:
            count_dict[each] = 1
        # else: increment value of key by 1
        else:
            count_dict[each] += 1
    return count_dict

# make a dictionary that has counts as keys and list of words as values
def sort_frequency(some_dict):
    # prime an empty dictionary
    sorted_dict = {}
    #create a word list from the dictionary argument
    word_list = some_dict.keys()
    #sort it alphabetically
    word_list.sort()
    #take each word from the word_list and sort it in the dictionary based on its count
    for word in word_list:
        value = some_dict[word]
        # check if the word's count is already a key. If it isn't create one and place the word in a list as the count's value.
        if sorted_dict.get(value, 0) == 0:
            sorted_dict[value] = [word]
        # if the word's count is already a key, append the word to the value list
        else:
            sorted_dict[value].append(word)
    return sorted_dict

def print_counts(some_dict):
    # make a list of keys and sort them by frequency
    keys = some_dict.keys()
    keys.sort()
    # print the key and value
    for key in keys:
        for each in some_dict[key]:
            print each, key  


opened = open_read_close(filename)
lowered = make_lower(opened)
separated = separate(lowered)
no_punctuation = strip_punctuation(separated)
counted = counts(no_punctuation)
s = sort_frequency(counted)
print_counts(s)
