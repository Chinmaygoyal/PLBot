import http.client
import os
from dotenv import load_dotenv

def updateAll():
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    load_dotenv()
    TOKEN = os.getenv('API_FOOTBALL_TOKEN')
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': TOKEN
        }

    conn.request("GET", "/fixtures?league=39&next=10&timezone=Asia/Kolkata", headers=headers)
    res = conn.getresponse()
    data = res.read()
    # Thes are the fixtures

    f = open("fixtures.txt", "w")
    f.write(data.decode("utf-8"))
    f.close()


    conn.request("GET", "/standings?league=39&season=2020", headers=headers)
    res = conn.getresponse()
    data = res.read()

    f = open("standings.txt", "w")
    f.write(data.decode("utf-8"))
    f.close()
# updateAll()