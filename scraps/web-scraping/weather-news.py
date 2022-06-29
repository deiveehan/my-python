
import requests

r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=51.049999&lon=-114.066666&appid=69404c7584393f52410cc2e957232d6e")
content = r.json()

print(content['weather'][0]['description'])



