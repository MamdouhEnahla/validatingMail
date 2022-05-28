
#importing regular expression module

import re

#vaild mail pattern
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_mail(mail):

    if (re.fullmatch(regex,mail)):
        return True
    return False

mail = input("Please enter a valid email : ")

if mail_check(mail):
    print("Valid email")
else:
    print("Sorry your email is invalid")
