#This sample produce an error

#filename = 'alice.txt'
#
#with open(filename, encoding='utf-8') as f:
#    contents = f.read()


#Error soln

#filename = 'alice.txt'
#
#try:
#    with open(filename, encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"Sorry the {filename} does not exist.")


#Analyzing Text

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words")


