"""Working with multiple files."""

#def count_words(filename):
#    """Count the approx number of words in a file."""
#    try:
#        with open(filename, encoding='utf-8') as f:
#            contents = f.read()
#    except FileNotFoundError:
#        print(f"Sorry, the file {filename} does not exist.")
#    else:
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {filename} has about {num_words} words.")
#filename = 'alice.txt'
#count_words(filename)


#We’ll try to count the words for Alice in Wonderland, Siddhartha, Moby Dick, and Little Women.

#def count_words(filename):
#    """Count the approx number of words in a file."""
#    try:
#        with open(filename, encoding='utf-8') as f:
#            contents = f.read()
#    except FileNotFoundError:
#        print(f"Sorry, the file {filename} does not exist.")
#    else:
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {filename} has about {num_words} words.")
#filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
#for filename in filenames:
#    count_words(filename)


"""Failing Silently."""

def count_words(filename):
    """Count the approx number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)