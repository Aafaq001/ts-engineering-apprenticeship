#fizzbuzz

def fizzbuzz(num:int) -> str:
    if num % 3 and num % 5 == 0:
        return "fizzbuzz"
    elif num%3 == 0 and num%5 != 0:
       return "fizz"
    elif num%3 != 0 and num%5 == 0:
            return "buzz"
    else:
         return num

#Palindrome number

def is_palindrome_string(num: int) -> bool:
    # Convert to string and compare with its reverse
    return str(num) == str(num)[::-1]

for num in range(1,11):
    palindrom_num = is_palindrome_string(num)
    fizzbuzz_num = fizzbuzz(num)
    print(f"{palindrom_num}")
    print(f"{fizzbuzz_num}")

#didn't do valid paranthesis will understand it also next time