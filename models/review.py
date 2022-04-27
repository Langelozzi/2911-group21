# Review class

'''A class to represent a single user review for a course'''

# Imports:
from models.user import User

class Review:
    def __init__(self, user: str, title: str, course: str, instructor: str, review: str, rating: int) -> None:
        if rating not in (1,2,3,4,5):
            raise ValueError
        # will add more checks in later sprints^
        
        self.user = user
        self.title = title
        self.course = course
        self.instructor = instructor
        self.content = review
        self.rating = rating 

    def to_dict(self) -> dict:
        return {
            "User": self.user,
            "Title": self.title,
            "Course": self.course,
            "Instructor": self.instructor,
            "Content": self.content,
            "Rating": self.rating
        }