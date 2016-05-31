import pytest
from check_phonenumber.service import CheckPhoneNumber

@pytest.fixture
def test_data():
    data = {
        "phone_number": "+40721234567",
        "country_code": "RO"
    }
    return data


def test_service(test_data):
    result = CheckPhoneNumber.validate_phone(data=test_data)
    assert result.get('valid_number') is True
