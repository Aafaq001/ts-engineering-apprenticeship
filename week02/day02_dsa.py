import json

from risk_utils import classify_risk, calculate_risk

with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)


numbers = [4, 8, 2, 15, 7]

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


def count_high_risk_users(users):
    high_risk_count = 0
    for user in users:
        score = calculate_risk(user["reports"], user["warnings"], user["bans"])
        level = classify_risk(score)
        if level == "high":
            high_risk_count += 1
    return high_risk_count


def find_highest_risk_user(users):
    
    highest_score = -1
    highest_risk_user = None
    for user in users:
        score = calculate_risk(user["reports"], user["warnings"], user["bans"])
        if score > highest_score:
            highest_score = score
            highest_risk_user = user["username"]
    return highest_risk_user,highest_score


print(f"Min: {find_min(numbers)}")
print(f"Max: {find_max(numbers)}")
print(f"High risk count: {count_high_risk_users(users)}")
print(f"Highest risk user: {find_highest_risk_user(users)}")