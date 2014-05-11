from sys import argv

def get_filenames(argv):
    #print argv
    if len(argv) < 2:
        print "No file specified."
    elif len(argv) > 2:
        filename = argv[1:]
        return filename
    else:
        script, filename = argv
        filename = [filename]
        return filename
#script, filename = argv
#print type(argv) ---- list
#print argv  ---- argv[0] is the script, argv[1] is the filename


# Open file and read. Output will be a string
def opening(some_file):
    f = open(some_file)
    filetext = f.read()
    f.close()
    return filetext

# Split the string at each new line. Return a list
def splitting(some_string):
    lines = some_string.split("\n")
    return lines

# is valid will check if there is something in the line and that the line is formatted properly
def isValidLine(some_string):
    #is there something in the line?
    if len(some_string) < 1:
        return False
    else:
         # check if the line is formatted properly (restaurant:rating).
         # TODO: perhaps check if the new strings will be valid as well. (Is the rating a valid integer)
        if ':' not in some_string and len(some_string.split(":")) != 2:
            return False
        else:
            return True
                #TODO: When the string is split by the colon if index 1 of the new list cannot be turned into an int
                # return False
                #if some_string.split(":")[1] isinstance of int:
                    #return True
                #else:
                    #return False


# Take a list and split each value in the list at : and place the right hand side as the key and left hand side as the value in a dictionary
def make_dict_listings(some_list):
    dictionary = {}
    for each in some_list:
        # Check if the line is valid (resturant:rating) by calling isValidLine()
        # if True, split at the : will return a list. By referencing the indexes of that list, you can create the dictionary
        if isValidLine(each):
            listing = each.split(":")
            key = listing[0]
            value = listing[1]
            dictionary[key] = int(value)
        else:
            del some_list[some_list.index(each)]
    return dictionary

# Take a dictionary. Make a list of all keys and sort those keys alphabetically. Then call those keys and print the rating.
# TODO: sort by rating
def print_sorted_dict(some_dict):
    restaurants = some_dict.keys()
    restaurants.sort()
    for restaurant in restaurants:
        rating = some_dict[restaurant]
        print "Restaurant %s is rated at %d" % (restaurant, rating)


        

# Call the necessary functions
def main(file_to_open):
    if file_to_open:
        count = 1
        for each in file_to_open:     
            print "Sorting file %d" % count         
            line_list = splitting(opening(each))
            restaurant_ratings = make_dict_listings(line_list)
            print_sorted_dict(restaurant_ratings)
            count += 1
    else:
        print "Program closing"
# notice that we're calling the get_filenames in this if clause.
# Python will automatically run it when it's called from the command line. 
# You could also just call main() and then have main get_filenames. 
if __name__ == "__main__":
    file_to_open = get_filenames(argv)
    main(file_to_open)