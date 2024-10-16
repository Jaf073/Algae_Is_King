# Name: Kaylee Matic
# Date: 10/14/2024
# Write a program that creates a 4 character code by comparing the
# epoch time to the current time

import sys
import time
import hashlib
import calendar

# function to convert the time given in string format to seconds 
def timeToSeconds(input):
    tempTime = time.strptime(input, "%Y %m %d %H %M %S")
    seconds = time.mktime(tempTime)
    tempTime = time.gmtime(seconds)
    seconds = calendar.timegm(tempTime)
    return (int)(seconds)

# constants
DEBUG = True
MANUAL_CURRENT_TIME = True
CURRENT_TIME = (int)(time.time())
EPOCH = (sys.stdin.read())
EPOCH = EPOCH.strip() #removes newline character

# if MANUAL_CURRENT_TIME is true -> able to control the current time
if (MANUAL_CURRENT_TIME):
    CURRENT_TIME = '2017 04 26 15 14 30'
    currInSec = timeToSeconds(CURRENT_TIME)

# printing epoch and current time
if (DEBUG):    
    print(f"Epoch time: {EPOCH}\nCurrent time: {CURRENT_TIME}")
    print("-----------------------------------")

# must convert the given epoch time to seconds
epochInSec = timeToSeconds(EPOCH)

# printing time in seconds
if (DEBUG):
    print(f"Epoch time in seconds: {epochInSec}")
    if (MANUAL_CURRENT_TIME):
        print(f"Current time in seconds: {currInSec}")
    else :
        print(f"Current time in seconds: {CURRENT_TIME}")
    print("-----------------------------------")

#### trail and error


# finding the difference between the epoch time and current time
if (MANUAL_CURRENT_TIME):
    timeElapsed = currInSec - epochInSec
else:
    timeElapsed = CURRENT_TIME - epochInSec

# printing the difference
if (DEBUG):
    print(f"The time elapsed is: {timeElapsed}")
    print("-----------------------------------")

# adjusting the difference so that code will work within a 60 second interval
timeElapsed = timeElapsed - (timeElapsed % 60)

# converting the time elapsed in the MD5 function
timeElapsed = (str)(timeElapsed)
hashed = hashlib.md5((timeElapsed.encode())).hexdigest()
hashed2 = hashlib.md5((hashed.encode())).hexdigest()

if (DEBUG):
    print(f"The MD5 hash: {hashed}")
    print(f"The MD5 double hash: {hashed2}")

# converting the hash to the code with the first 2 letters from left-to-right
# and the first 2 numbers from right-to-left
code = ''

# finding first 2 letters
count = 0
for character in hashed2:
    c = ord(character)
    if (c >= 97 and c <= 102):
        code += character
        count += 1
    if (count == 2):
        break

# reversing the hash and finding the first 2 numbers
count = 0
reverseHashed2 = "".join(reversed(hashed2))
for character in reverseHashed2:
    c = ord(character)
    if (c >= 48 and c <= 57):
        code += character 
        count += 1
    if (count == 2):
        break

# printing the final code
print(code)