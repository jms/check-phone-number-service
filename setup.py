from setuptools import setup, find_packages

setup(
    name='check-phone-number',
    version='1.0',
    url="https://github.com/jms/check-phone-number",
    author="Jeronimo Martinez Sanchez",
    author_email="jms@rz0r.net",
    description="Bottle microservice to verify phone numbers",
    py_modules=['main', 'check_phonenumber.service'],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ]
)
