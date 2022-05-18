# Review class

'''A class to represent a single user review for a course'''

# Imports:
import datetime

class Review:
    '''class to represent a review object'''
    
    def __init__(self, id: str, user_email: str, title: str, course: str, instructor: str, review: str, rating: int, date: str) -> None:
        """constructor method that sets variables and will do data checking

        Args:
            user_email (str): the email the user logs in with
            title (str): the title of the review
            course (str): what course the review is for
            instructor (str): who taught the course
            review (str): the content of the review. the details
            rating (int): a score out of 5
            date (str): the date the review was written. format: MM-DD-YYYY

        Raises:
            ValueError: if the rating is not a number from 1-5
            ValueError: if the title, course, instructor name or review content contains a bad word
        """
        
        # checking that the rating is 1-5
        if rating not in (1,2,3,4,5):
            raise ValueError

        # bad word checking
        bad_words = ["ass", "asshole", "dick", "dingus", "idiot", "cunt", "fuck", "shit", "nigger", "nigga", "bitch", "bastard", "retard", "wanker", "loser", "damn", "twat"]
        all_words = f"{title} {course} {instructor} {review}"
        word_list = all_words.split()

        bad_in_all_words = [word for word in word_list if word.lower() in bad_words]
        if len(bad_in_all_words) != 0:
            raise ValueError
        
        # will add more checks in later sprints^
        self.id = id
        self.user_email = user_email
        self.title = title
        self.course = course
        self.instructor = instructor
        self.content = review
        self.rating = rating 
        # converts the string date that was passed in, into a date object of format 2022-04-22 00:00:00
        self.date = datetime.datetime.strptime(date, '%m-%d-%Y %H:%M')


    def to_dict(self) -> dict:
        """Method to transform the review into a dictionary for json purposes

        Returns:
            dict: the dictionary with the review info
        """
        
        return {
            "Id": self.id,
            "UserEmail": self.user_email,
            "Title": self.title,
            "Course": self.course,
            "Instructor": self.instructor,
            "Content": self.content,
            "Rating": self.rating,
            "Date": self.date.strftime('%m-%d-%Y %H:%M')
        }

    def edit(self, title: str, course: str, instructor: str, content: str, rating: int):
        """Method that alters title, course, instructor, content or rating of a review

        Args:
            title (str): the title of the review
            course (str): the course its written for
            instructor (str): the person who teaches the course
            content (str): the review content
            rating (int): the rating out of 5

        Raises:
            ValueError: if the rating is not 1-5
        """
        
        # checking that the rating is 1-5
        if rating not in (1,2,3,4,5):
            raise ValueError
        
        self.title = title
        self.course = course
        self.instructor = instructor
        self.content = content
        self.rating = rating
        # sets time of review to the time and date that it was edited
        self.date = datetime.datetime.now()
