filename = 'programming_poll.txt'

print("Enter a reason why you like programming.")
print("Type 'q' when you are finished")

while True:
    reason = input("Enter why you like programming: ")

    if reason == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{reason}\n")