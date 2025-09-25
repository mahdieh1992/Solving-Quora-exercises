#بِسَنج!
#import re
def validate_email(email):
    # validate email with regex
    pattern_email = r'([a-zA-Z0-9._]+)@([a-zA-Z0-9]+).([a-zA-Z]{3})$'
    if re.match(pattern_email,email):
        return True
    else:
        return False

def validate_phone(phone):
    # validate phone with regex
    pattern_phone = r'^(09|\+989|00989)[0-9]{9}$'
    if re.match(pattern_phone,phone):
        return True
    else:
        return False
import re
def validate_email(email):
    # validate email with regex
    pattern_email = r'([a-zA-Z0-9._]+)@([a-zA-Z0-9]+).([a-zA-Z]{3})$'
    if re.match(pattern_email,email):
        return True
    else:
        return False

def validate_phone(phone):
    # validate phone with regex
    pattern_phone = r'^(09|\+989|00989)[0-9]{9}$'
    if re.match(pattern_phone,phone):
        return True
    else:
        return False


email = input()
phone = input()
print(validate_email(email))
print(validate_phone(phone))