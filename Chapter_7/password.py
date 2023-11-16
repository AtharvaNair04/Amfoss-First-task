import re
length=re.compile(r'.{8,}')
upper=re.compile(r'[A-Z]')
lower=re.compile(r'[a-z]')
digit=re.compile(r'[0-9]')
def check(text):
    if length.search(text) is None:
        return False
    if upper.search(text) is None:
        return False
    if lower.search(text) is None:
        return False
    if digit.search(text) is None:
        return False
    else:
        return True
password=input("Enter password:")
if check(password) is True:
    print("Strong password.Great job!")
else:
    print("Weak password, try again")
