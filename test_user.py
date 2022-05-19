import pytest
from models.user import User
from models.review_collection import ReviewCollection
from unittest.mock import patch, mock_open



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

@pytest.fixture
def user():
    return User(
        "hello",
        "simon freeman",
        "sfreeman@my.bcit.ca",
        "polodunga"
    )


def test_bad_user():
    with pytest.raises(ValueError):
        bad_user = User("", "", "@my.sfu.ca", "")


def test_good_user(user):
    assert user.public_id == "hello"
    assert user.name == "simon freeman"
    assert user.email == "sfreeman@my.bcit.ca"
    assert user.password == "polodunga"


def test_to_dict(user):
    
    dict = {
        "Id": "hello",
        "Name": "simon freeman",
        "Email": "sfreeman@my.bcit.ca",
        "Password": "polodunga",
    }
    assert user.to_dict() == dict


def test_get_reviews(user, review_collection):
    correct_list = user.get_reviews(review_collection)
    assert "something@my.bcit.ca" not in [
        rev for rev in correct_list]

# def test_save():
#     saving = user.save()
#     assert saving in dummy_data