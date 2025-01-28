import re
import json

#--------------------------------------------------------------------------
# NOTE : R String in python

# Normal string
normal_string = "This is a newline:\nNext line."
# print(normal_string)

# Raw string
raw_string = r"This is a newline:\nNext line."
# print(raw_string)
#--------------------------------------------------------------------------

email_pattern = '\\w+@\\w*\\.(com|ir|org)'

text = 'I am AmirAli my Email is : amirali@gmail.com'

# if you have multuplie ithems that macth with pattern 'search' function just return the first item
# if not find any thing return None

email = re.search(email_pattern, text)

# to get founded ithem with pattern call group() function for item

# if email:
#     E = email.group()
#     print(f"Extracted email: {E}")
# else:
#     print("No email found.")

#--------------------------------------------------------------------------

text2 = "My email is amirali@gmail.com. Please contact me at amirali@example.ir or info@organization.org."
pattern = '\\w+@\\w*\\.\\w+'

# return a list of items that match with pattern

emails = re.findall(pattern, text2)

# if emails:
#     print("Extracted emails:")
#     for email in emails:
#         print(email)
# else:
#     print("No emails found.")

#--------------------------------------------------------------------------

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)

# returns a tuple containing the start-end, and end positions of the match.
# print(x.span())

# returns the string passed into the function
# print(x.string)

# returns the part of the string where there was a match
# print(x.group())

#--------------------------------------------------------------------------

# read numbers from json file

pattern = '[0-9]+'

with open('sample4.json', 'r') as jsonFile:
    jsonData = json.load(jsonFile)

jsonTxt = json.dumps(jsonData)

nums = re.findall(pattern, jsonTxt)

if nums:
    print('The Numbers in File : ')
    for num in nums:
        print(num)
else:
    print('No numbers found')