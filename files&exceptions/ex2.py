with open('learning_python.txt') as file_object:
    content = file_object.readlines()
    for line in content:
        line = line.replace('Python', "C")
        print(line.strip())

