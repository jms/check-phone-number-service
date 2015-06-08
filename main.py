from bottle import Bottle, run, error, request, response, debug
import phonenumbers
from phonenumbers import carrier, NumberParseException

app = Bottle()


@app.route('/', method='GET')
def hello():
    return "Check Phone micro service"


@app.route('/check-phone', method='POST')
def check_phone():
    try:
        data = request.json
        phone_number = data['phone_number']
        cc = data['country_code']
        # print(data)
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

    response.content_type = 'application/json'
    return check_result

@error(404)
def error404(error):
    return 'Release the Kraken'


debug(True)
run(app, host='localhost', port=8080)
