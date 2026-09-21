# exercise 1

i=1
for i in range(1, 11):
    print(f"user {i}")

# exercise 2
scores = [10, 25, 42, 67, 83, 91]
for i in scores:
    if i <= 25:
        print(f"{i} - low")
    elif i <= 50:
        print(f"{i} - medium")
    elif i <= 75:
        print(f"{i} - high")
    else:
        print(f"{i} - Critical")

# exercise 3

reports = [2, 5, 12, 3, 18, 1, 22]
total_reports = 0
scores = 0
highest = 0
lowest = reports[0]

for i in reports:
    scores = scores + i;
    total_reports += 1
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print(f"Total Reports: {total_reports}")
average = scores / len(reports)
print(f"Average: {round(average)}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# exercise 4

i= 5
while i >= 0:
    print(i)
    i -= 1
print("Done!")

# exercise 5

users = [
    "ali",
    "john",
    "sara",
    "hamza",
    "ahmed"
]

for i in users:
    print(f"processing {i}")
    if i == "sara":
        break

# exercise 6

reports = [4, 0, 7, 0, 12, 3]

for i in reports:
    if i == 0:
        continue
    print(f"{i}")

    #we use for loop to iterate though list when items are known.
    #we user while when a certain condition is met.
    #counter is used to keep track of a loop or number and is  also used to control the loop to a certain number of iterations.
    #accumulator is used to keep track of a toal or a sum of a certain value.
    #when while condition is never met it goes on in a never ending loop.
    #Break is used to exit a loop or when a certain condition is met.
    #Continue is used to skip a certain iteration of a loop when a certain condition is met.
    # Can you write a loop from a blank file without looking at an example? had a bit difficulty in understanding this question but to my understanding, i can write a loop 1st i'll put conditoin if length is notzero then i will proceed for the iteration.