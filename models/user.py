# User class

'''A class to represent a single user'''

class User:
    def __init__(self, id: str, full_name: str, email: str, password: str) -> None:
        self.public_id = id
        self.name = full_name
        self.email = email
        self.password = password

    def change_password(self, old_pass, new_pass) -> bool:
        if old_pass == self.password:
            self.password = new_pass
            return True
        else:
            return False