with open("week01/testfile.txt", "w") as testing:
    testing.write("This is the initial text.")

with open("week01/testfile.txt", "r") as testing:
    print(testing.read())

with open("week01/testfile.txt", "a") as testing:
    testing.write(" This is the appended text.")

with open("week01/testfile.txt", "r") as testing:
    print(testing.read())