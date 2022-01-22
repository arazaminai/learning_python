#! python3
# Phone_Email - Pulls Phone numbers and Emails from clipboard

# import paperclip as pc
import re
import requests


try:
    site_text = requests.get(input()).text
    # site_text = site.text
except requests.exceptions.MissingSchema:
    print("Invalid Site")
    exit()

#Phone Number
try:
    phone_number = re.compile(r"(0)(\s)?(\d{3})(\s)?(\d{3})(\s)?(\d{2})(\s)?(\d{2})")
    string = phone_number.search(site_text).group()
    # string2 = ""

    # for k, v in enumerate(string):
    #     if v == " " or v == None:
    #       string.pop(k) 
    
    # string = string.join()

    print(string)

except AttributeError:
    print("There is no phone number")

#Email
email = re.compile(r"""
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
\.[a-zA-Z]{2,4}
""")
try:
    du = email.search(site_text).group()
    print(du)
except AttributeError:
    print("There is no Email")