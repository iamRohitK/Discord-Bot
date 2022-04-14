import discord
import os
from dotenv import load_dotenv
import requests   # This module allows our code to make an HTTP request to get data from the API. The API returns json.
import random
from replit import Database

load_dotenv()  
Token = os.getenv('TOKEN')
db = Database(db_url=os.getenv('DATABASE'))     # Type this "$REPLIT_DB_URL" command in replit shell command to get replit databse

# Create an instance of a client
# This is a connection to discord
client = discord.Client()

sad_words = ["sad", "depressed", "depressing", "angry", "unhappy", "miserable"]
starter_encouragement = [
    "Cheer Up!",
    "Hang in there.",
    "You are a great person."
]

if "responding" not in db.keys():
    db["responding"] = True

def get_quote():
    response = requests.get("https://zenquotes.io/api/random").json()
    quote = response[0]['q'] + " -" + response[0]['a']
    return quote

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

# A Python decorator is a function that takes in another function, adds some functionality to it, and then returns it. 
# A decorator acts as a wrapper to other functions
@client.event     # event = A decorator that registers an event to listen to
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # Do not do anything if the message is from bot itself
    if message.author == client.user:
        return

    msg = message.content
    
    # if the message starts with a command that's being sent to discord bot
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if db["responding"]:
        options = starter_encouragement
        if 'encouragements' in db.keys():
            options += db['encouragements']

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]     # split() method ref: https://www.geeksforgeeks.org/python-string-split/
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message has been added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split('$del', 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"].value
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"].value
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ",1)[1]
        
        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

client.run(Token)   