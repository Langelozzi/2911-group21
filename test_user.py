import email
import pytest
from models.user import User


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



def test_return_user_review():
    pass