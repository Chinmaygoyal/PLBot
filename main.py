import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import teamStandings
import fixtures
from TeamDictionary import teamDict
from TeamDictionary import teamID
import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!',description="Premier League bot")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='standings',help='Gives the current standings of the Premier League')
async def standings(context):
    embed=discord.Embed(title="Premier League Standings", 
    description=teamStandings._make_table(teamStandings.getStandings()), color=discord.Color.blue())
    await context.send(embed = embed)

def getLeagueFixtures():
    # Return the embed
    fixturelist = fixtures.getFixtures()
    embed=discord.Embed(title="Premier League Fixtures",
    color=discord.Color.blue())
    for obj in fixturelist:
        teams = obj[4] + " v/s " + obj[5]
        details = "Venue: " + obj[0] + "\n" + "Date: " + obj[1] + "\n" + "Time: " + obj[2] + "\n" + "Round: " + obj[3]
        embed.add_field(name=teams, value=details, inline=False)
    return embed

def getTeamNameFromMsg(msg):
    msg = msg.split(" ",1)[1]
    teamName = msg
    if msg in teamDict.keys() or msg in teamDict.values():
        teamName = msg
        if msg in teamDict.values():
            # This is in the form of "MUN"
            for longName in teamDict:
                if teamDict[longName] == msg:
                    teamName = longName
                    break
    else:
        teamName = "FALSE"
    return teamName

@bot.command(name='fixtures',help='Gives the next 10 fixtures of the Premier League')
async def fixture(context):
    # check if some team name is given or not
    msg = context.message.content
    if " " in msg:
        # This is not empty hello
        teamName = getTeamNameFromMsg(msg)
        print(teamName)
        if teamName == "FALSE":
            await context.send("Team name not valid")
            await context.send(embed = getLeagueFixtures())
        else:
            # Have a valid team name
            # Find the team id from json
            id = -1
            id = teamID[teamName]
            if id == -1:
                await context.send("Team name not valid")
                await context.send(embed = getLeagueFixtures())
            # have a valid team id
            print(id)
            await context.send(embed = getLeagueFixtures())
    else:
        # This is empty hello so give the main fixture list
        await context.send(embed = getLeagueFixtures())

keep_alive.keep_alive()
bot.run(TOKEN)