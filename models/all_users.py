# class representing all the users in the database

# Imports
import json
from models.user import User
from werkzeug.security import check_password_hash

class AllUsers:
    def __init__(self) -> None:
        # opening the json file and loading the data
        with open("./data/users.json", "r") as file:
            data = json.load(file)

            # attribute with list of all Users
            self.users = [
                # list comprehension to create User objects from each json data entry
                User(usr["Id"], usr["Name"], usr["Email"], usr["Password"]) 
                for usr in data
            ]
    
    def get_user_by_name(self, name):
        return [
            usr for usr in self.users 
            if name in usr.name
        ]
        
    def get_user_by_email(self, email):
        return [
            usr for usr in self.users
            if usr.email == email
        ][0]

    def identify_user(self, email, password):
        try:
            user = self.get_user_by_email(email)
            verified = check_password_hash(user.password, password)

            if verified:
                return user
            else:
                return False
        except:
            return False

    def get_user_by_id(self, id):
        return [
            usr for usr in self.users
            if id == usr.public_id
        ][0]

