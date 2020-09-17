import lichess.api
import random
import discord
from discord.ext import commands
import time
import asyncio
from covid import Covid
from fuzzywuzzy import process

# id = 559392094351917076
messages = 0
joined = 0
bot = commands.Bot(command_prefix="-")
murdered = {}


class CovidData:
    def __init__(self):
        self.covid = Covid()
        self.covid_update_time = None
        self.update_covid_data()

    def update_covid_data(self):
        if (
            not self.covid_update_time
            or time.time() - self.covid_update_time >= 3600
        ):
            self.covid.get_data()
            self.covid_update_time = time.time()
        self.country_list = [el["name"] for el in self.covid.list_countries()]

    @property
    def country_name(self):
        self.update_covid_data()
        return self.country_list

    def __getattr__(self, name):
        def fn(*args):
            self.update_covid_data()
            return getattr(self.covid, name)(*args)

        return fn


covid = Covid(source="worldometers")


client = discord.Client()


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("statts.txt", "a") as f:
                f.write(
                    f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n"
                )

                messages = 0
                joined = 0

                await asyncio.sleep(300)
        except Exception as e:
            print(e)
            await asyncio.sleep(300)


@client.event
async def on_ready():
    print("Logged in...")
    print("Username: " + str(client.user.name))
    print("Client ID: " + str(client.user.id))


@client.event
async def on_message(message):
    args = message.content.split(" ")
    if args[0] == "-antichess":
        name = " ".join(args[1:])
        try:
            user = lichess.api.user(name)
        except:
            return await message.channel.send("user not found")
        await message.channel.send((user["perfs"]["antichess"]["rating"]))
    elif args[0] == "-atomic":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["atomic"]["rating"]))
    elif args[0] == "-bullet":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["bullet"]["rating"]))
    elif args[0] == "-blitz":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["blitz"]["rating"]))
    elif args[0] == "-rapid":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["rapid"]["rating"]))
    elif args[0] == "-classical":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["classical"]["rating"]))
    elif args[0] == "-crazyhouse":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["crazyhouse"]["rating"]))
    elif args[0] == "-chess960":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["chess960"]["rating"]))
    elif args[0] == "-kingOfTheHill":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["kingofthehill"]["rating"]))
    elif args[0] == "-threeCheck":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["threeCheck"]["rating"]))
    elif args[0] == "-horde":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["horde"]["rating"]))
    elif args[0] == "-racingKings":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["racingkings"]["rating"]))
    elif args[0] == "-ultrabullet":
        name = " ".join(args[1:])
        user = lichess.api.user(name)
        await message.channel.send((user["perfs"]["ultrabullet"]["rating"]))
    if message.content == "-github":
        await message.channel.send(
            "https://github.com/Maj0rites/Maj0rs-lichess-bot"
        )
    elif message.content == "-help":
        await message.channel.send("My prefix is - for more info type -info")
    elif message.content == "-info":
        await message.channel.send(
            "```-github ~ Shows the github link of bot \n -author ~ shows who made that bot \n -bullet [nickname] ~ Shows the [nickname]'s bullet rating \n -blitz [nickname] ~ Shows the [nickname]'s blitz rating \n -rapid [nickname] ~ Shows the [nickname]'s rapid rating \n -classical [nickname] ~ Shows the [nickname]'s classical rating \n -crazyhouse [nickname] ~ Shows the [nickname]'s crazyhouse rating \n  -chess960 [nickname] ~ Shows the [nickname]'s chess960 rating \n -kingOfTheHill [nickname] ~ Shows the [nickname]'s king of the hill rating \n -threeCheck [nickname] ~ Shows the [nickname]'s threeCheck rating \n -antichess [nickname] ~ Shows the [nickname]'s antichess rating \n -atomic [nickname] ~ Shows the [nickname]'s atomic rating \n -horde [nickname] ~ Shows the [nickname]'s horde rating \n -racingKings [nickname] ~ Shows the [nickname]'s racingKings rating \n -ultrabullet [nickname] ~ Shows the [nickname]'s ultrabullet rating \n Usage : -antichess AskMeWhoAmI \n -[variant]Tv sends [variant's] lichess Tv link!```"
        )
    elif message.content == "-author":
        await message.channel.send(f"""hit 'em up#0011""")
    elif message.content.startswith("-random "):
        args = message.content.split(" ")[1:]
        await message.channel.send(random.choice(args))
    elif message.content == ("-antichessTv"):
        await message.channel.send("https://lichess.org/tv/antichess")
    elif message.content == ("-bulletTv"):
        await message.channel.send("https://lichess.org/tv/bullet")
    elif message.content == ("-blitzTv"):
        await message.channel.send("https://lichess.org/tv/blitz")
    elif message.content == ("-rapidTv"):
        await message.channel.send("https://lichess.org/tv/rapid")
    elif message.content == ("-classicalTv"):
        await message.channel.send("https://lichess.org/tv/classical")
    elif message.content == ("-crazyhouseTv"):
        await message.channel.send("https://lichess.org/tv/crazyhouse")
    elif message.content == ("-chess960Tv"):
        await message.channel.send("https://lichess.org/tv/chess960")
    elif message.content == ("-kingOfTheHillTv"):
        await message.channel.send("https://lichess.org/tv/kingOfTheHill")
    elif message.content == ("-threeCheckTv"):
        await message.channel.send("https://lichess.org/tv/threeCheck")
    elif message.content == ("-antichessTv"):
        await message.channel.send("https://lichess.org/tv/antichess")
    elif message.content == ("-atomicTv"):
        await message.channel.send("https://lichess.org/tv/atomic")
    elif message.content == ("-hordeTv"):
        await message.channel.send("https://lichess.org/tv/horde")
    elif message.content == ("-racingKingsTv"):
        await message.channel.send("https://lichess.org/tv/racingKings")
    elif message.content == ("-ultraBulletTv"):
        await message.channel.send("https://lichess.org/tv/ultraBullet")
    elif message.content == ("-computerTv"):
        await message.channel.send("https://lichess.org/tv/computer")
    elif message.content == ("-botTv"):
        await message.channel.send("https://lichess.org/tv/bot")
    elif message.content.startswith("-murder"):
        global murdered
        if message.mentions[0].id in murdered:
            if murdered[message.mentions[0].id]["time"] + 90 > time.time():
                return await message.channel.send(
                    "```You have already murdered him wait for 90 seconds```"
                )
        murdered[message.mentions[0].id] = {}
        murdered[message.mentions[0].id]["time"] = time.time()
        embed = discord.Embed()
        embed.add_field(
            name="I will murder you!", value="Job done!", inline=False
        )
        await message.channel.send(embed=embed)
    elif message.content == ("-covid deaths"):
        await message.channel.send(covid.get_total_deaths())
    elif message.content == ("-covid confirmed"):
        await message.channel.send(covid.get_total_confirmed_cases())
    elif message.content.startswith("-covid"):
        try:
            country_name = message.content.split()[1]
        except IndexError:
            await message.channel.send(
                "Usage: -covid [deaths | confirmed | <country>]"
            )
            return
        try:
            data = covid.get_status_by_country_name(country_name)
            msg = f'{country_name}: Confirmed cases: {data["confirmed"]} Deaths: {data["deaths"]} Recovered: {data["recovered"]}'
            await message.channel.send(msg)
        except ValueError:
            country_guess = process.extract(country_name, covid.country_list)
            msg = "Sorry, I couldn't recognize {}. Did you mean {} or {}?".format(
                country_name, country_guess[0][0], country_guess[1][0]
            )
            await message.channel.send(msg)


client.loop.create_task(update_stats())
client.run("Ur token")
