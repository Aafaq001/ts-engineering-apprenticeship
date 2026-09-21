name = input("Enter your name: ")
time = int(input("Enter time in seconds of a mile run: "))
gender = input("Enter gender (M/F): ")
one = True

if  ((time <= 560 and gender.upper() == "M") or (time <= 720 and gender.upper() == "F")):
    print(f"Congrats {name}, you passed!")
else:
    print(f"Keep Practicing, {name}!")

print(not one) #just for not operator demonstration