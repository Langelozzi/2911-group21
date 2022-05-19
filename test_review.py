import pytest
from models.review import Review
import datetime


@pytest.fixture
def review():
    return Review(
        "bd071262-eeea-4c78-955b-66aaaaf57908",
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
        bad_review = Review("", "", "", "", "", "", 6, "")


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
        "Id": "bd071262-eeea-4c78-955b-66aaaaf57908",
        "UserEmail": "jsmith@my.bcit.ca",
        "Title": "Loved this course!!!",
        "Course": "ACIT 2911",
        "Instructor": "Johnny Zhang",
        "Content": "This course is fantastic!",
        "Rating": 5,
        "Date": "04-20-2022 18:00"
    }
    assert review.to_dict() == review_dict

    # hello = review.to_dict()

    # assert hello["Title"] == "Loved this course!!!"


def test_edit(review):
    assert review.title == "Loved this course!!!"
    assert review.course == "ACIT 2911"
    assert review.instructor == "Johnny Zhang"
    assert review.content == "This course is fantastic!"
    assert review.rating == 5

    review.edit("Love it!!", "ACIT 2000",
                "Lucas Longanizelli", "Cest Magnifique", 4)

    assert review.title == "Love it!!"
    assert review.course == "ACIT 2000"
    assert review.instructor == "Lucas Longanizelli"
    assert review.content == "Cest Magnifique"
    assert review.rating == 4


def test_bad_edit(review):
    with pytest.raises(ValueError):
        review.edit("Love it!!", "ACIT 2000",
                    "Lucas Longanizelli", "Cest Magnifique", 6)


def test_bad_word():
    with pytest.raises(ValueError):
        review = Review("wufw20", "jsmith@my.bcit.ca", "twat",
                        "ACIT 2911", "Bob", "bitch cunt", 4, "04-20-2022 18:00")
