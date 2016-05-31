import phonenumbers
from phonenumbers import carrier, NumberParseException


class CheckPhoneNumber:
    @staticmethod
    def validate_phone(data):
        try:
            phone_number = data.get('phone_number')
            cc = data.get('country_code')
            number_data = phonenumbers.parse(phone_number, cc)
            check_possible_number = phonenumbers.is_possible_number(number_data)
            check_valid_number = phonenumbers.is_valid_number(number_data)
            carrier_info = carrier.name_for_number(number_data, "en")
            carrier_data = str(carrier_info)
            check_result = {
                "number_data": str(number_data),
                "possible_number": check_possible_number,
                "valid_number": check_valid_number,
                "carrier_data": carrier_data
            }
        except NumberParseException:
            check_result = {"success": False, "message": "Number not valid or no possible"}
        except KeyError:
            check_result = {"success": False, "message": "key missing on json data"}
        return check_result
