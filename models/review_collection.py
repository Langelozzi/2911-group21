# Review collection class

'''A class to represent the collection of all the reviews in the JSON file'''

# Imports
import json
from xmlrpc.client import DateTime
from models.review import Review
import datetime


class ReviewCollection:
    '''Class for a collection of all reviews in the JSON file'''

    def __init__(self) -> None:
        """Constructor method. Imports all the reviews from the json and turns them into 
        review objects.
        """

        # opening the json file and loading the data
        with open("./data/reviews.json", "r") as file:
            data = json.load(file)

            # attribute with list of all reviews
            self.reviews = [
                # list comprehension to create Review objects from each json data entry
                Review(rev["UserEmail"], rev["Title"], rev["Course"],
                       rev["Instructor"], rev["Content"], rev["Rating"], rev["Date"])
                for rev in data
            ]

            # calling the sort_by_date function to display the reviews in descending order by default (newest to oldest)
            self.sort_by_date(self.reviews, rev=True)

    def get_reviews_as_dicts(self) -> list:
        """Converts all the Review objects to dictionaries and returns them
        as a list.

        Returns:
            list: a list of all the reviews as dicts
        """

        # list comprehension to create dictionaries from each Review object
        dict_reviews = [review.to_dict() for review in self.reviews]
        return dict_reviews

    def get_review_by_course(self, course: str) -> list:
        """Get a list of reviews for a single course

        Args:
            course (str): the course the reviews are for

        Returns:
            list: all the reviews in the database for that course
        """

        # using .lower() so that the searched are case insensitive
        # using 'in' so that acit1515 results in acit 1515 reviews. aka, less sensitive searching
        course_reviews = [
            rev for rev in self.reviews
            if course.lower() in rev.course.lower()
        ]

        return course_reviews

    def get_review_by_instr(self, instr: str) -> list:
        """Get a list of reviews for a course taught by a specific instructor

        Args:
            instr (str): the instructor who teaches the courses you are searching for

        Returns:
            list: all the reviews in the database for that courses taught by that instructor
        """

        # using .lower() so that the searched are case insensitive
        # using 'in' so that "johnny" results in reviews of any instructor named johnny, regardless of last name
        instr_reviews = [
            rev for rev in self.reviews
            if instr.lower() in rev.instructor.lower()
        ]

        return instr_reviews

    def sort_by_date(self, lst: list, rev: bool) -> bool:
        """Sorts a list of objects with a date attribute by their date.

        Args:
            lst (list): the list of objects to be sorted
            rev (bool): whether or not to reverse the list. rev=False gives small to big. rev=True gives big to small

        Returns:
            bool: if the list was successfully sorted or not
        """

        try:
            # sorting the list by the objects dates
            lst.sort(key=lambda item: item.date, reverse=rev)
            return True
        except:
            return False

    def add_review(self, user, title: str, course: str, instructor: str, review: str, rating: int):
        # user_email = user.email
        # date = datetime.datetime.now()
        
        # try:
        #     new_review = Review(user_email, title, course, instructor, review, rating, date)
        #     self.reviews.append(new_review)
        #     return new_review
        # except:
        #     return False

