
#importing regular expression module

import re

#vaild mail pattern

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def mail_check(mail):

    valid = False

    if (re.fullmatch(regex,mail)):
        valid = True

    return valid
mail = input("Please enter your email : ")

if mail_check(mail):
    print("Valid email")
else:
    print("Sorry your email is invalid")
