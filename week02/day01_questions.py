#1 - List is mutable and tuple is not mutable. This means that you can change the contents of a list, but you cannot change the contents of a tuple. For example, you can add or remove elements from a list, but you cannot do the same with a tuple.
#2 - i would use a tuple when i need a data that would not be changed like list of days in a week or list of months in a year etc
#3 - set cannot have duplicate values while a list has duplicate values.
#4 - set is useful for membership checks because it allows for fast lookups have unique elements.
#5 - dictionary is in the form of key-value pairs. i think it is useful when we have repeated data against a unique key.
#6 - if we retrieve data using user["country"] it might throw error if key country is not present in dictionary while user.get("country") will return None if key is not present in dictionary.
#7 - .item() returns us a list of dictiony in key-value pair format.
#8 - .keys() returns us a list of all the keys in the dictionary.
#9 - .values() returns us a list of all the values in the dictionary.
#10 - it contains other data structures in one data structure. like list of dictionaries. lists within a list etc.
#11 - list comprehension is more readable and faster than for loop.
#12 - it will return all the usernames from a dictionary of users using an object user.
#13 - we add condition to filter out the data we want. like from a list of all the users we can get only banned users by using condition.
#14 - dictionary comprehension is easy to use and save unnecessary variable creation. it is more readable and faster than for loop.
#15- i would use a set i dont want duplicate value.
#16 - main advantage is we can store data in key-value pair and access data using specific key instead of index.
#17 - it can lead to inconsistency and confusion if we have multiple keys with same value. it can also lead to data loss if we overwrite a key with new value.
#18 - 
# a -> list - mutable, indexed
# b-> set - because we dont want duplicate values and set don't allow duplicate values.
# c -> dictionary - we want to store data in key-value pair username : risk_score
# d -> tuple - tuple values are immutable and we don't want to change threshold.