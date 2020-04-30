import requests

day = 3  # Day -> range(0,6)

response = requests.get(f"https://e82437da.ngrok.io/cafeapi/food?day={day}")
data = response.json()

print(data)
