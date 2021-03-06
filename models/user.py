# User class

'''A class to represent a single user'''

import json
from models.review_collection import ReviewCollection


class User:
    def __init__(self, id: str, full_name: str, email: str, password: str) -> None:
        """Constructor method for a user object 

        Args:
            id (str): the random generated uuid
            full_name (str): the first and last name of the user
            email (str): the users preferred email address
            password (str): the users encrypted password 
        """

        if email[-11:] != "@my.bcit.ca":
            raise ValueError("Email must be a mybcit email")
        
        self.public_id = id
        self.name = full_name
        self.email = email
        self.password = password

    # def change_password(self, old_pass, new_pass) -> bool:
    #     if old_pass == self.password:
    #         self.password = new_pass
    #         return True
    #     else:
    #         return False

    def to_dict(self) -> dict:
        """Return the User information as a dictionary

        Returns:
            dict: the user info as a dict
        """
        
        return {
            "Id": self.public_id,
            "Name": self.name,
            "Email": self.email,
            "Password": self.password 
        }

    def save(self) -> None:
        """Saves the "self" user object into the user.json file
        """
        
        # create a list with the (new) user as the first item
        all_users = [self.to_dict()]
        
        # import the list of dictionaries from the json file and add each on to the all_users list
        with open("data/users.json", "r") as file:
            data = json.load(file)
            for user in data:
                all_users.append(user)
        
        # write the all_users list to the json file
        with open("data/users.json", "w") as file:
            json.dump(all_users, file)

    def get_reviews(self, collection: ReviewCollection) -> list:
        """Get all the reviews written by the user

        Args:
            collection (ReviewCollection): the collection of all the reviews

        Returns:
            list: a list of all the reviews written by that user
        """
        
        return [rev for rev in collection.reviews if self.email.lower() == rev.user_email]