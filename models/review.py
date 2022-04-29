# Review class

'''A class to represent a single user review for a course'''

# Imports:
from models.user import User
import datetime

class Review:
    '''class to represent a review object'''
    
    def __init__(self, user_email: str, title: str, course: str, instructor: str, review: str, rating: int, date: datetime) -> None:
        """constructor method that sets variables and will do data checking

        Args:
            user_email (str): the email the user logs in with
            title (str): the title of the review
            course (str): what course the review is for
            instructor (str): who taught the course
            review (str): the content of the review. the details
            rating (int): a score out of 5

        Raises:
            ValueError: if the rating is not a number from 1-5
        """
        
        # checking that the rating is 1-5
        if rating not in (1,2,3,4,5):
            raise ValueError
        # will add more checks in later sprints^
        
        self.user_email = user_email
        self.title = title
        self.course = course
        self.instructor = instructor
        self.content = review
        self.rating = rating 
        self.date = date


    def to_dict(self) -> dict:
        """Method to transform the review into a dictionary for json purposes

        Returns:
            dict: the dictionary with the review info
        """
        
        return {
            "UserEmail": self.user_email,
            "Title": self.title,
            "Course": self.course,
            "Instructor": self.instructor,
            "Content": self.content,
            "Rating": self.rating
        }