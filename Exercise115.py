#بازی پول
import re
import hashlib
class Account:
    def __init__(self, username: str, password: str, national_id: str, phone: str, email: str) -> None:
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.national_id = self.id_validation(national_id)
        self.phone = self.phone_validation(phone) 
        self.email = self.email_validation(email)

    def username_validation(self, username: str) -> str:
        pattern = r'[a-zA-Z]+_[a-zA-Z]+'
        if re.fullmatch(pattern,username):
            return username
        else:
            raise ValueError("Invalid username.")

    def password_validation(self, password: str) -> str:
        if len(password) >= 8 and re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[0-9]',password):
            encoded = password.encode("utf-8")
            hash_pass = hashlib.sha256(encoded)
            password = hash_pass.hexdigest() 
            return password  
        else:
            raise ValueError("Invalid password.")

    def id_validation(self, id: str) -> str:
        if len(id) < 10 or not id.isdigit():
             raise ValueError( "Invalid national id.")
        j = 10
        sum_number = 0
        for num in id:
            if j == 1:
                break
            if num == '0':
                sum_number += 0
                j -= 1
            else:
                sum_number += int(num) * j
                j -= 1
        result = sum_number % 11
        num_control = int(id[-1])
        if result < 2  and result == num_control:
            return id
        elif result >= 2 and (11 - result) == num_control:
            return id 
        else:
            raise ValueError( "Invalid national id.")
                
    def phone_validation(self, phone: str) -> str:
        pattern = r'^(\+989|09)[0-9]{9}'
        if re.fullmatch(pattern,phone):
            phone = '09'+ phone[-9:]
            return phone
        else:
            raise ValueError("Invalid phone number.")

    def email_validation(self, email: str) -> str:
        pattern = r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+\.[a-zA-Z]{2,5}$'
        if re.fullmatch(pattern,email):
            return email
        else:
            raise ValueError("Invalid email.")

    def set_new_password(self, password: str) -> None:
        try:
            password = self.password_validation(password)
            return password
        except ValueError:
            raise ValueError("Invalid password.")
        

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

class Site:
    
    
    def __init__(self, url_address: str) -> None:
        self.url_address = url_address
        self.registered_users = []
        self.active_users = []

    def register(self, user: Account) -> str:
        if self.registered_users:
            for registered_user in self.registered_users:
                if registered_user.username == user.username:
                   raise ValueError("User already registered.")
        self.registered_users.append(user)
        return "Register successful."
    
    def login(self, username: str = None, email: str = None, password: str = None) -> str:
        if password is None or (username is None and email is None):
            return "Invalid login."
        
        encoded = password.encode('utf-8')
        hash_pass = hashlib.sha256(encoded)
        pass_hex = hash_pass.hexdigest()
        
        for user in self.registered_users:
            if pass_hex == user.password and (username == user.username or email == user.email):
                if user in self.active_users:
                    return "User already logged in."
                else:
                    self.active_users.append(user)
                    return "Login successful."
        return "Invalid login."
           
    def logout(self, user) -> str:
        ...

    def __repr__(self):
        return f"Website URL: {self.url}\nRegistered users: {self.register_users}\nActive users: {self.active_users}"

    def __str__(self):
        return self.url



def show_welcome(func):
    ...


def verify_change_password(func):
    ...


@show_welcome
def welcome(user):
    return f"Welcome to our website {user}!"


@verify_change_password
def change_password(user, old_pass, new_pass):
    return "Your password has been changed successfully."


# account1 = Account('ali_babai','Aabbccdd12','0024848484','09133747009','ali.babaei-123@company.amni')
# sit = Site("https://www.google.com")

# sit.register(account1)
# print(sit.registered_users)
