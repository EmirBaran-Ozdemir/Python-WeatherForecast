import requests

city = input('input the city name\n')
print(city)

print('Displaying Weather report for: ' + city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)