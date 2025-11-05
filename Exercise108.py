#کتابخانه‌ی برهم
import requests

def add_book(book: dict[str, str]) -> str | None:
    url_list = {'mathematics':'http://127.0.0.1:8000/mathematics/',
               'physics':'http://127.0.0.1:8000/physics/',
               'chess':'http://127.0.0.1:8000/chess/'}
    category = book['category']
    if category not in url_list:
        return "Invalid Category"
    else:
        url = url_list[category]
        response = requests.get(url)
        try:
            data = response.json()
        except ValueError:
            return "Bad Request"
        if book in data:
            return "Bad Request"
        else:
            json_data = book
            requests.post(url,json=json_data)
    
book = {"name": "book_name", "category": "physics"}
print(add_book(book))
    