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

conn.request("GET", "/fixtures?league=39&next=10&team=33&timezone=Asia/Kolkata", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
