import email
from xmlrpc.client import DateTime
import pytest
from models.review_collection import ReviewCollection
from unittest.mock import patch, mock_open
import datetime
from models.user import User

from test_review import review

dummy_data = '''
    [
        {
            "UserEmail": "jsmith@my.bcit.ca",
            "Title": "Loved this course!!!",
            "Course": "ACIT 2911",
            "Instructor": "Johnny Zhang",
            "Content": "This course is fantastic!",
            "Rating": 5,
            "Date": "04-20-2022 18:00"
        },
        {
            "UserEmail": "mtang@my.bcit.ca",
            "Title": "It was alright",
            "Course": "ACIT 1620",
            "Instructor": "Alex Lau",
            "Content": "This course is quite challenging when you dont have much experience with web coding. Still passed though!",
            "Rating": 3,
            "Date": "04-12-2022 10:30"
        },
        {
            "UserEmail": "jbrooker@my.bcit.ca",
            "Title": "Super fun course!",
            "Course": "ACIT 2811",
            "Instructor": "Yves Rene Shema",
            "Content": "This course really allowed us to express our creativity! You learn about User centered design and go through the process in a group of 3.",
            "Rating": 5,
            "Date": "04-27-2022 09:18"
        }
    ]
'''


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=dummy_data)
def review_collection(mock_file):
    """This functions is a fixture that returns a mock file object

    Args:
        mock_file (_type_): mock file object

    Returns:
        _type_: mock file object
    """
    return ReviewCollection()


def test_length(review_collection):
    """This function tests the length of the review collection

    Args:
        review_collection (ReviewCollection): a review collection object
    """
    assert len(review_collection.reviews) == 3


def test_values(review_collection):
    """This function tests the values of the review course and email in the review collection

    Args:
        review_collection (ReviewCollection): a review collection object
    """
    assert review_collection.reviews[0].course == "ACIT 2811"
    assert review_collection.reviews[0].user_email == "jbrooker@my.bcit.ca"

    assert review_collection.reviews[1].course == "ACIT 2911"
    assert review_collection.reviews[1].user_email == "jsmith@my.bcit.ca"

    assert review_collection.reviews[2].course == "ACIT 1620"
    assert review_collection.reviews[2].user_email == "mtang@my.bcit.ca"


def test_review_by_course(review_collection):
    """This functions tests the length of the list, and checks the review course 

    Args:
        review_collection (ReviewCollection): a review collection object
    """
    correct_list = review_collection.get_review_by_course("ACIT 2811")

    assert len(correct_list) == 1
    assert correct_list[0].course == "ACIT 2811"
    assert "ACIT 2911" not in [rev.course for rev in correct_list]
    assert "ACIT 1620" not in [rev.course for rev in correct_list]


def test_review_by_instr(review_collection):
    """This function tests the length of the instructor review and checks the value

    Args:
        review_collection (ReviewCollection): a review collection object
    """
    correct_list_instr = review_collection.get_review_by_instr(
        "Yves Rene Shema")

    assert len(correct_list_instr) == 1
    assert correct_list_instr[0].instructor == ("Yves Rene Shema")
    assert "Johnny Zhang" not in [
        rev.instructor for rev in correct_list_instr]
    assert "Alex Lau" not in [
        rev.instructor for rev in correct_list_instr]


def test_to_dicts(review_collection):
    """This function tests the values of the content in the review collection, and also checks
    if it is a dictionary

    Args:
        review_collection (ReviewCollection): a review collection object
    """
    correct = {
        "UserEmail": "jbrooker@my.bcit.ca",
        "Title": "Super fun course!",
        "Course": "ACIT 2811",
        "Instructor": "Yves Rene Shema",
        "Content": "This course really allowed us to express our creativity! You learn about User centered design and go through the process in a group of 3.",
        "Rating": 5,
        "Date": datetime.datetime.strptime("04-27-2022 09:18", '%m-%d-%Y %H:%M')
    }

    dict_list = review_collection.get_reviews_as_dicts()
    assert type(dict_list[0]) == dict
    assert correct["Content"] in [d["Content"] for d in dict_list]


def test_sort_by_date(review_collection):
    """This function tests sorting by date, and returns false if there is no date

    Args:
        review_collection (ReviewCollection):a review collection object
    """
    for obj in review_collection.reviews:
        obj.date = None

    sorted = review_collection.sort_by_date(review_collection, True)

    assert sorted == False

def test_add_review(review_collection):
    """This function tests if review has been added to the review collection list"""
    #add a review to the review collection and save that review to the json file
    #take everything that is passed in, add to review object, then add to review collection list    
    review_collection = ReviewCollection()

    title_add = review_collection.add_review(user = "fake@my.bcit",title="Good Course", course="ACIT 2911", instructor="Johnny Zhang",review="Johnny was lovely",rating=5)
    assert title_add.user == "fake@my.bcit"
    assert title_add.title == "Good Course"
    assert title_add.course == "ACIT 2911"
    assert title_add.instructor == "Johnny Zhang"
    assert title_add.content == "Johnny was lovely"
    assert title_add.rating == 5

    assert type(review.date) == DateTime
    
    assert review in review_collection.reviews
    pass


    # course_add = review_collection.add_review(course="ACIT 2911")
    # assert review.course == "ACIT 2911"

    # instructor_add = review_collection.add_review(instructor="Johnny Zhang")
    # assert review.instructor == "Johnny Zhang"

    # review_add = review_collection.add_review(review="Johnny was lovely")
    # assert review.review == "Johnny was lovely"

    # rating_add = review_collection.add_review(rating=5)
    # assert review.rating == 5

    


def test_save_reviews(review_collection):
    #will need mocking
    #mock open json fill
    pass