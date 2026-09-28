#1 - In except block we can handle the error and display custom error message.
#2 - we use try/except to control/validate the data in try we test block of code and in except we control error.
#3 - its better cuz we know what we are controlling/testing instead of bare expect and masking unknown bugs and errors with no clear indication of error and over writing the error.
#4 - Valueerror means the value is incorrect but data type is correct like expecting number but user passing abc & index error can be like asking for 10 item in the while having only 5 items in a list.
#5 - finally block always runs in the last whether try/except pass or fail.
#6 - instead of whole program running completely even though it detected the error raise forcefully stops program with message of error we encountered.
#7 - we need to validate data before running the process to check whether data itself is correct instead of false processing.
#8 - python module is a whole file ending with file type .py
#9 - import fetches the file of the files content we need instead of writing the again in the current file.
#10 - import module import the whole file and its all data and everything is accessible in the file while from module import function import specific function we need in our current file instead of all the data we dont even need
#11 - we dont want to keep file always open and close it manually all the time sometimes we do so we use with open(...) 
#12 - "r" means to just read the file we cannot modify or write the file "w" means to write content in the file and it removes all previous data and "a" appends data in the file next to previous data in the file.
#13 - json.load() parses the json file into python native list or dictionary for easy processing
#14 - json.dump() parses/writes python data back into json text format with key argument obj = python data we want to save fp = the opened file where the data will go and indent = spaces for clear insertion
#15 - I think json is important because its easy to use and easy to retrieve/store data with clear data.