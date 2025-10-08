import re
#اسپم
# this is check number if only number is it's True
def check_sender(number) -> bool:
    if number.isdigit():
        return True
    else:
        return False
# check content if content contain 0-9a-zA-Z _ and spam exists in content it's true 
def check_content(content: str) -> bool:
    pattern = r'[^0-9a-zA-Z _]'
    lContent = len(content) // 2
    lExept = len(re.findall(pattern,content))
    spam = re.findall(r'spam',content.lower())
    if lExept > lContent and len(spam) != 0:
        return True
    else:
        return False
# this function for result of check_content and check_number
def result(number,content):
    global check_sender,check_content
    check_sender = check_sender(number)
    check_content = check_content(content)
    if not check_sender  and not check_content:
        return "Not Spam"
    elif check_sender and not check_content:
        return "Invalid Sender"
    elif not check_sender and check_content:
        return "Invalid Content"
    else:
        return "Fully Invalid"
number = input()
content = input()      
print(result(number,content))