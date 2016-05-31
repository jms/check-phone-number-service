
# check-phone-number-service [![Build Status](https://travis-ci.org/jms/check-phone-number-service.svg?branch=master)](https://travis-ci.org/jms/check-phone-number-service)
microservice to check phone numbers using libphonenumber  and the python port python-phonenumbers

Test data
```json
{
    "phone_number": "+40721234567",
    "country_code": "RO"
}
```

Run the service:

```bash
$ python main.py
```

Testing using httpie:

```bash
$ http POST localhost:8080/check-phone < test_data.json
```

```bash
HTTP/1.0 200 OK
Content-Length: 137
Content-Type: application/json
Date: Thu, 19 May 2016 23:53:32 GMT
Server: WSGIServer/0.1 Python/2.7.10

{
    "carrier_data": "Vodafone", 
    "number_data": "Country Code: 40 National Number: 721234567", 
    "possible_number": true, 
    "valid_number": true
}
```
