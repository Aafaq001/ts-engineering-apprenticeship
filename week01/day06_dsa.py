#fizzbuzz

def fizzbuzz(num:int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num%3 == 0:
       return "fizz"
    elif num%5 == 0:
            return "buzz"
    else:
         return str(num)

#Palindrome number

def is_palindrome_string(num: int) -> bool:
    # Convert to string and compare with its reverse
    return str(num) == str(num)[::-1]

for num in range(1,16):
    print(f"{fizzbuzz(num)}")

for num in range(1,16):
    print(f"{is_palindrome_string(num)}")

#valid paranthesis

def is_valid_replace(s: str) -> bool:
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

print(is_valid_replace("()"))
print(is_valid_replace("()[]{}"))
print(is_valid_replace("{[]}"))
print(is_valid_replace("(]"))
print(is_valid_replace("([)]"))
print(is_valid_replace("{"))
