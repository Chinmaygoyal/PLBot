import json
import table
import discord
from TeamDictionary import teamDict

def getStandings(sortby = ""):
    teamlist = []
    with open('standings.txt', 'r') as handle:
        # temp = json.load(handle)
        # print(temp)
        parsed = json.load(handle)["response"][0]["league"]["standings"][0]
        # print(parsed)
        sortbyID = 0
        standingsHeader = ['rank', 'name', 'mp', 'w', 'd', 'l', 'gf', 'ga', 'pts', 'form']
        if sortby.lower() in standingsHeader:
            sortbyID = standingsHeader.index(sortby.lower()) 
            
        for obj in parsed:
            newTeam = []
            newTeam.append(obj["rank"])
            newTeam.append(teamDict[obj["team"]["name"]])
            newTeam.append(obj["all"]["played"])
            newTeam.append(obj["all"]["win"])
            newTeam.append(obj["all"]["draw"])
            newTeam.append(obj["all"]["lose"])
            newTeam.append(obj["all"]["goals"]["for"])
            newTeam.append(obj["all"]["goals"]["against"])
            newTeam.append(obj["points"])
            newTeam.append(obj["form"])
            teamlist.append(newTeam)
    ascsort = sortby.isupper()
    teamlist.sort(key = lambda x: x[sortbyID],reverse = ascsort) 
    return teamlist

def _make_table(teamlist):
    
    style = table.Style('{:>}  {:<}  {:<}  {:<}  {:<}  {:<}  {:<} {:<}  {:<}  {:<}')
    t = table.Table(style)
    t += table.Header('Rank', 'Name', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'Pts', 'Form')
    t += table.Line()
    for team in teamlist:
        t += table.Data(team[0] , team[1], team[2], team[3],team[4] , team[5], team[6], team[7],team[8],team[9])
    table_str = '```\n'+str(t)+'\n```'
    return table_str


print(getStandings())