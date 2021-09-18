import requests


x = requests.get(
    url='http://ddns.example.com/set',
    params={'host': 'test_host'},
    auth=('test_user', 'password')
)
print(x.status_code, x.text)
