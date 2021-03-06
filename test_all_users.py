import pytest
from models.all_users import AllUsers
from models.user import User
from models.review_collection import ReviewCollection
from unittest.mock import patch, mock_open

# "Howdy1234!"
dummy_data = ''' [
    {
        "Id": "91e28efe-5fa3-4bea-8eca-76587b20cd1e",
        "Name": "Joe Smith",
        "Email": "jsmith@my.bcit.ca",
        "Password": "pbkdf2:sha256:260000$4bcYiZqNJxObgAUJ$dcbec52ca27858e0556dcad1ae0cd8422e1909d741c82bdea6188a1f7b5b616f"
    },
    {
        "Id": "8da671ab-fb7f-4cec-a6d4-7d4cb1d0c53e",
        "Name": "Lucas Angelozzi",
        "Email": "langelozzi@my.bcit.ca",
        "Password": "Goodbye4321!"
    },
    {
        "Id": "5307a183-31f6-44c8-847c-4a1b3a257885",
        "Name": "John Doe",
        "Email": "jdoe@my.bcit.ca",
        "Password": "Itadakimasu2@"
    }
] '''


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=dummy_data)
def all_users(mock_file):
    """This functions is a fixture that returns a mock file object

    Args:
        mock_file (_type_): mock file object

    Returns:
        _type_: mock file object
    """
    return AllUsers()


def test_length_all_users(all_users):
    assert len(all_users.users) == 3


def test_get_user_by_name(all_users):
    correct_user = all_users.get_user_by_name("Joe Smith")
    assert "Joe Smith" in [usr.name for usr in correct_user]


def test_get_user_by_email(all_users):
    correct_email = all_users.get_user_by_email("jsmith@my.bcit.ca")
    assert correct_email.email == "jsmith@my.bcit.ca"


def test_user_by_id(all_users):
    correct_id = all_users.get_user_by_id(
        "91e28efe-5fa3-4bea-8eca-76587b20cd1e")
    assert correct_id.public_id == "91e28efe-5fa3-4bea-8eca-76587b20cd1e"


def test_identify_user(all_users):
    user = all_users.identify_user("jsmith@my.bcit.ca", "Howdy1234!")
    assert user.email == "jsmith@my.bcit.ca"
    assert user.name == "Joe Smith"
    assert user.public_id == "91e28efe-5fa3-4bea-8eca-76587b20cd1e"


def test_bad_identify_user(all_users):
    user = all_users.identify_user("jsmith@my.bcit.ca", "Howdy")
    assert user == False


def test_bad_identify_user2(all_users):
    user = all_users.identify_user("js@my.bcit.ca", "Howdy")
    assert user == False
