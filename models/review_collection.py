# Review collection class

'''A class to represent the collection of all the reviews in the JSON file'''

# Imports
import json
from models.review import Review

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
                Review(rev["UserEmail"], rev["Title"], rev["Course"], rev["Instructor"], rev["Content"], rev["Rating"])
                for rev in data
            ]

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