#کتابخانه‌ی درهم
import requests
import json

def find_category(url: str) -> str:
    try:
        response = requests.get(url)
    except requests.RequestException:
        return "Bad Request"
    if response.status_code != 200:
        return "Bad Request"
    try:
        data = response.json()
    except ValueError:
        return "Bad Request"
    if len(list(data)) > 0:
        final_list = set(book['category'] for book in data)
        if len(final_list) == 1:
            result = "".join(final_list)
            return result
        else:
            return "I can't recognize it"
    else:
        return "I can't recognize it"
       
url = "http83af-4eb932811d5c"
print(find_category(url))
