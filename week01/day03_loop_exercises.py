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
sum = 0
highest = 0
lowest = 100

for i in reports:
    sum = sum + i;
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print(f"Total Reports: {len(reports)}")
average = sum / len(reports);
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