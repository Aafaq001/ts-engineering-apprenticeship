users = [
    "alex_dev",
    "samira_tech",
    "mike_codes",
    "luna_writer",
    "noor_dev"
]

users.append("omar_builder")
user = users.remove("luna_writer")
users.insert(1, "john_codes")

print(f"{users}")
print(f"User at index 1: {users[1]}")
print(f"User at last index: {users[-1]}")

users.sort()
print(f"Sorted alphabetically: {users}")

users.reverse()
print(f"List reversed: {users}")
print(f"Total users: {len(users)}")