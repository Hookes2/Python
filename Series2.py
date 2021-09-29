#Password Checker

user_name = input('What is your username? ')
password = input('What is your password? ')
password_length = len(password)
hash_password = '*' * password_length

print(f'Hey {user_name}, your password {hash_password} is {password_length} characters long!')