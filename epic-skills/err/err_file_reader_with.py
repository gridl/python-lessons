try:
    with open('1example_text.txt', 'r') as file:
        contents = file.read()
    print(contents)
except:
    print ("Error opening file")
