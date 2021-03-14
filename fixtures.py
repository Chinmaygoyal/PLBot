import json

def getTime(time):
    temp = time.split("T",1)
    temp = temp[1]
    temp = temp.split("+",1)[0]
    return temp

def getDate(time):
    temp = time.split("T",1)
    temp = temp[0]
    # temp = temp.split("+",1)[0]
    temp = temp.split("-")
    finalDate = temp[2] + "-" + temp[1] + "-" + temp[0]
    return finalDate

def getFixtures(id1=0):
    fixturelist = []
    with open('fixtures.txt', 'r') as handle:
        parsed = json.load(handle)["response"]
        for obj in parsed:
            if(obj["teams"]["away"]["id"] == id1 or obj["teams"]["home"]["id"] == id1 or id1==0):
                newmatch = []
                # Venue,Date,Time,Round,HomeTeam,AwayTeam
                newmatch.append(obj["fixture"]["venue"]["name"])
                newmatch.append(getDate(obj["fixture"]["date"]))
                newmatch.append(getTime(obj["fixture"]["date"]))
                newmatch.append(obj["league"]["round"].split("-")[1])
                newmatch.append(obj["teams"]["home"]["name"])
                newmatch.append(obj["teams"]["away"]["name"])
                fixturelist.append(newmatch)
        # print(json.dumps(parsed[0], indent=4))
    if(len(fixturelist) == 0):
        fixtureslist = ['No Matches Found']
    return fixturelist

# match = getFixtures()[0]
# print(getDate(match[1]))
# print(fixturelist)
# for fixture in fixturelist:
#     print(fixture)