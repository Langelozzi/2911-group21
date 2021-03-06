import pytest
from models.review_collection import ReviewCollection
from models.review import Review
from unittest.mock import patch, mock_open
import datetime
from models.user import User

dummy_data = '''
    [
        {
            "Id": "1feeab52-29c3-45ce-a396-73c15f9da36f",
            "UserEmail": "jsmith@my.bcit.ca",
            "Title": "Loved this course!!!",
            "Course": "ACIT 2911",
            "Instructor": "Johnny Zhang",
            "Content": "This course is fantastic!",
            "Rating": 5,
            "Date": "04-20-2022 18:00"
        },
        {
            "Id": "f6f75a63-8dfe-414f-a75f-4d54c4732ea6",
            "UserEmail": "mtang@my.bcit.ca",
            "Title": "It was alright",
            "Course": "ACIT 1620",
            "Instructor": "Alex Lau",
            "Content": "This course is quite challenging when you dont have much experience with web coding. Still passed though!",
            "Rating": 3,
            "Date": "04-12-2022 10:30"
        },
        {
            "Id": "bd071262-eeea-4c78-955b-66aaaaf57908",
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
        "Id": "bd071262-eeea-4c78-955b-66aaaaf57908",
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
    lucas = User("abcd123", "Lucas Angelozzi",
                 "langelozzi@my.bcit.ca", "P@ssw0rd")

    new_review = review_collection.add_review(
        id="62e6a2b4-427f-494d-aa70-b9b88f4a98b0",
        user=lucas,
        title="This course is awesome haha!",
        course="ACIT 2811",
        instructor="Yves Rene Shema",
        review="This course is really cool, highly recommend",
        rating=5
    )

    assert type(new_review) == Review
    assert new_review in review_collection.reviews


def test_add_review_contents(review_collection):
    lucas = User("abcd123", "Lucas Angelozzi",
                 "langelozzi@my.bcit.ca", "P@ssw0rd")

    new_review = review_collection.add_review(
        id="62e6a2b4-427f-494d-aa70-b9b88f4a98b0",
        user=lucas,
        title="This course is awesome haha!",
        course="ACIT 2811",
        instructor="Yves Rene Shema",
        review="This course is really cool, highly recommend",
        rating=5
    )

    assert new_review.user_email == "langelozzi@my.bcit.ca"
    assert new_review.title == "This course is awesome haha!"
    assert new_review.course == "ACIT 2811"
    assert new_review.instructor == "Yves Rene Shema"
    assert new_review.content == "This course is really cool, highly recommend"
    assert new_review.rating == 5
    assert type(new_review.date) == datetime.datetime


def test_add_review_bad_review(review_collection):
    lucas = User("abcd123", "Lucas Angelozzi",
                 "langelozzi@my.bcit.ca", "P@ssw0rd")

    new_review = review_collection.add_review(
        id="62e6a2b4-427f-494d-aa70-b9b88f4a98b0",
        user=lucas,
        title="This course is awesome haha!",
        course="ACIT 2811",
        instructor="Yves Rene Shema",
        review="This course is really cool, highly recommend",
        rating=13  # a rating not in 1-5 should return a valueerror triggering the except block in the add_review function which returns False
    )

    assert new_review == False


def test_save_reviews(review_collection):
    # will need mocking
    # mock open json fill
    pass


def test_get_review_by_id(review_collection):
    review = review_collection.get_review_by_id(
        "1feeab52-29c3-45ce-a396-73c15f9da36f")

    assert review.title == "Loved this course!!!"
    assert review.content == "This course is fantastic!"


def test_bad_id(review_collection):
    review = review_collection.get_review_by_id(
        "1feeab52-29c3-456")
    assert review == False


def test_delete_review(review_collection):
    assert "1feeab52-29c3-45ce-a396-73c15f9da36f" in [
        rev.id for rev in review_collection.reviews]

    review = review_collection.delete_review(
        "1feeab52-29c3-45ce-a396-73c15f9da36f"
    )
    assert review == True
    assert "1feeab52-29c3-45ce-a396-73c15f9da36f" not in [
        rev.id for rev in review_collection.reviews]


def test_no_review_delete(review_collection):

    review = review_collection.delete_review(
        "1feeab52-29c3-45ce-a396-73c15f9da36"
    )
    assert review == False


def test_get_average_rating(review_collection):
    review_collection.add_review(
        "idlol", User("haha", "sdfdlfkfd", "apple@my.bcit.ca", "cheese"), "lol", "ACIT 2911", "bob", "good", 4)

    avg = review_collection.get_average_rating("ACIT 2911")
    assert avg == float(4.5)


def test_all_averages(review_collection):
    # avgs = {
    #     "ACIT 2911": 5,
    #     "ACIT 1620": 3,
    #     "ACIT 2811": 5
    # }

    all_avgs = review_collection.all_averages()

    assert "ACIT 2911" in all_avgs.keys()
    assert "ACIT 2811" in all_avgs.keys()
    assert "ACIT 1620" in all_avgs.keys()

    assert 5 in all_avgs.values()
    assert 3 in all_avgs.values()
