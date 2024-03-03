import json
from werkzeug.security import generate_password_hash, check_password_hash

# User data file
USER_DATA_FILE = 'users.json'

def hash_password(password):
    return generate_password_hash(password)

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def signup(email, name, password):
    users = load_users()
    if email in users:
        return False  # User already exists
    hashed_password = hash_password(password)
    users[email] = {'name': name, 'password': hashed_password}
    save_users(users)
    return True

def login(email, password):
    users = load_users()
    if email in users and check_password_hash(users[email]['password'], password):
        return email, users[email]['name']
    else:
        print("Incorrect email or password.")
        return None, None

def authenticate_user():
    choice = input("Do you have an account? (yes/no): ").lower()
    if choice == 'yes':
        return login()
    else:
        return signup()
