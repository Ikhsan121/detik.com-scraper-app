import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.4373161409248e-5,"date":"Sat, 29 Oct 2022 11:55:01 GMT","inverseRate":15534.424255515},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.4635424147589e-5,"date":"Sat, 29 Oct 2022 11:55:01 GMT","inverseRate":15471.392246403}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])