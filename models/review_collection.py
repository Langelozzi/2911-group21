# Review collection class

'''A class to represent the collection of all the reviews in the JSON file'''

# Imports
import json
from models.review import Review

class ReviewCollection:
    def __init__(self) -> None:
        with open("./data/reviews.json", "r") as file:
            data = json.load(file)

            self.reviews = [
                Review(rev["User"], rev["Title"], rev["Course"], rev["Instructor"], rev["Content"], rev["Rating"])
                for rev in data
            ]

    def get_reviews_as_dicts(self):
        dict_reviews = [review.to_dict() for review in self.reviews]
        return dict_reviews