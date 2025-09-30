#ثبت‌نام
def check_registration_rules(**users):
    list_users = []
    for username,password in users.items():
        if not (len(username) < 4) and not (len(password) < 6 or password.isdigit()) and username not in ('quera','codecup'):
            list_users.append(username)
    return list_users

print(check_registration_rules(saeed='1234567', ab='afj$L12'))