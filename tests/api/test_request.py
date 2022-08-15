import requests


def test_http_code200():
    r = requests.get('https://api.github.com/users/defunkt')
    print(r.__dict__)
