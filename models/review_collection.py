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