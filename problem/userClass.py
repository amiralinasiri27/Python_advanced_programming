import re
from database import *
from hash import hashFunction

class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = hashFunction(password)
        self.email = User.getEmail(email)
        self.id = get_num_of_users() + 1 

    def passwordValidation(password):
        return len(password) >= 8
    
    def usernameValidation(username):
        return len(username) >= 4
    
    def getEmail(email):
        email_pattern = '\\w+@\\w*\\.(com|ir|org)'
        currectEmail = re.search(email_pattern, email)
        if (currectEmail):
            return currectEmail.group()
        else:
            return None
