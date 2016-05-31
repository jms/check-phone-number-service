from bottle import Bottle, run, error, request, response, debug
from check_phonenumber.service import CheckPhoneNumber

app = Bottle()


@app.route('/', method='GET')
def index():
    return "Get Phone Number Information service"


@app.route('/check-phone', method='POST')
def check_phone():
    data = request.json
    check_result = CheckPhoneNumber.validate_phone(data)
    response.content_type = 'application/json'
    return check_result


@error(404)
def error404(error):
    return error


debug(True)
run(app, host='localhost', port=8080)
