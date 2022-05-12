import email
import pytest
from models.all_users import AllUsers
from models.user import User
from models.review_collection import ReviewCollection
from unittest.mock import patch, mock_open

dummy_data = ''' [
    {
        "Id": "91e28efe-5fa3-4bea-8eca-76587b20cd1e",
        "Name": "Joe Smith",
        "Email": "jsmith@my.bcit.ca",
        "Password": "sha256$b7QCMW5vqi96RvQH$071915866d88d949a8416510310b9a7c4966f67e96472b48a02d9d112e1dd3fc"
    },
    {
        "Id": "8da671ab-fb7f-4cec-a6d4-7d4cb1d0c53e",
        "Name": "Lucas Angelozzi",
        "Email": "langelozzi@my.bcit.ca",
        "Password": "sha256$tFegpSWp0SlFFIAa$203c91b9d280c32fff4d00224c6975d3e55a386188e9e245b058a43205adacb4"
    },
    {
        "Id": "5307a183-31f6-44c8-847c-4a1b3a257885",
        "Name": "John Doe",
        "Email": "jdoe@my.bcit.ca",
        "Password": "sha256$CiQDhqwJAnDBRHZQ$58df0d5fee3535d8d2600204c8c098bc14f1aaae44821152a8af3406627542a1"
    }
] '''

@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=dummy_data)
def review_collection(mock_file):
    """This functions is a fixture that returns a mock file object

    Args:
        mock_file (_type_): mock file object

    Returns:
        _type_: mock file object
    """
    return AllUsers()



def test_length_all_users(all_users):
    
    

