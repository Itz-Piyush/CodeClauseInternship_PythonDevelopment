#CODECLAUSE PVT LTD
#Python Development Intern
#August-2023
#Task-1
'''Random Pssword Generator in Python '''

#SOURCE CODE

import random
import string

def generate_password(username, length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    random.seed(username)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    username = input("Enter your username: ")
    password_length = int(input("Enter the desired password length: "))
    
    password = generate_password(username, password_length)
    print("Generated Password:", password)

#OUTPUT FORMAT
''' Enter your username: Piyush Raj
Enter the desired password length: 8
Generated Password: \V)w=J)f '''
