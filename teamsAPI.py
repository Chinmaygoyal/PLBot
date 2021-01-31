import http.client
import os
from dotenv import load_dotenv

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

load_dotenv()
TOKEN = os.getenv('API_FOOTBALL_TOKEN')
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': TOKEN
    }

conn.request("GET", "/teams?league=39&season=2020", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
