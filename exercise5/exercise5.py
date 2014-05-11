from sys import argv

"""
when you run python in the terminal, you can specify the script and filename 
that you would like to execute in the command line: Example, 
python exercise5.py twain.txt
"""
script, filename = argv


def letter_count(j):
    # open file, assign contents to variable filetext and make all letters lowercase
    f = open(j)
    filetext = f.read()
    f.close()
    filetext = filetext.lower()

    # create a new list and 26 indexes --- 0 will prime the indexes for the count
    count = []
    for i in range(97, 123):
        count.append(0)

    # for each character in filetext, check that the ascii # is in range(97, 123)
    # this will weed out punctuation 97 = 'a' 122 = 'z'
    for every in filetext:
        if ord(every) in range(97, 123):
            # to get the index of every subtract it by 97 so 'a' will now equal 0 
            index = ord(every) - 97
            # increment the count in the list
            count[index] += 1
        else:
            pass

    # prints out the count of each letter in the file in alphabetical order
    for number in count:
        print number


# calling the function
letter_count(filename)
