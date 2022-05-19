import pytest
from models.review import Review
import datetime


@pytest.fixture
def review():
    return Review(
        "jsmith@my.bcit.ca",
        "Loved this course!!!",
        "ACIT 2911",
        "Johnny Zhang",
        "This course is fantastic!",
        5,
        "04-20-2022 18:00"
    )


def test_bad_review():
    with pytest.raises(ValueError):
        bad_review = Review("", "", "", "", "", 6, "")


def test_good_review(review):
    assert review.user_email == "jsmith@my.bcit.ca"
    assert review.title == "Loved this course!!!"
    assert review.course == "ACIT 2911"
    assert review.instructor == "Johnny Zhang"
    assert review.content == "This course is fantastic!"
    assert review.rating == 5


def test_date(review):
    date = "04-20-2022 18:00"
    assert review.date == datetime.datetime.strptime(date, '%m-%d-%Y %H:%M')


def test_to_dict(review):
    review_dict = {
        "UserEmail": "jsmith@my.bcit.ca",
        "Title": "Loved this course!!!",
        "Course": "ACIT 2911",
        "Instructor": "Johnny Zhang",
        "Content": "This course is fantastic!",
        "Rating": 5
    }
    assert review.to_dict() == review_dict

    # hello = review.to_dict()

    # assert hello["Title"] == "Loved this course!!!"


def test_edit_review(review):
    pass


def test_delete_review(review):
    pass
