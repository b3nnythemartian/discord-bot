import discord
import logging

discord.utils.setup_logging()

token = "MTExMTU4NzI4NzI5ODQ3NDA2NQ.GAIeAa.XHb6qaWOrFUHHc_G7pTU3emB9tVt57x32ZdVjg"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

tally = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0};


# Assume client refers to a discord.Client subclass...

def increment(message): 
    key = ""
    if message == "+increment 1":
        key = "1"
    elif message == "+increment 2":
        key = "2"
    elif message == "+increment 3":
        key = "3"
    elif message == "+increment 4":
        key = "4"
    elif message == "+increment 5":
        key = "5"
    else:
        return 1

    tally[key] = tally[key] + 1
    return 1

def decrement(message): 
    key = ""
    if message == "+decrement 1":
        key = "1"
    elif message == "+decrement 2":
        key = "2"
    elif message == "+decrement 3":
        key = "3"
    elif message == "+decrement 4":
        key = "4"
    elif message == "+decrement 5":
        key = "5"
    else:
        return 1

    if (tally[key] != 0):
        tally[key] = tally[key] - 1

    return 1

def print_tally():
    return f"Ratings: Amount...\n1️⃣: {tally['1']} 2️⃣: {tally['2']} 3️⃣: {tally['3']} 4️⃣: {tally['4']} 5️⃣: {tally['5']}"



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    if reaction.message.author == client.user:
        if reaction.emoji == '1️⃣':
            increment('+increment 1')
        elif reaction.emoji == '2️⃣':
            increment('+increment 2')
        elif reaction.emoji == '3️⃣':
            increment('+increment 3')
        elif reaction.emoji == '4️⃣':
            increment('+increment 4')
        elif reaction.emoji == '5️⃣':
            increment('+increment 4')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('+bot'):
        await message.channel.send("Hi, I'm the EduConnect Market Research Bot. I'm here to help you with your market research. Type +help for more information. To increase the tally you can react with any of these emojis to adjust the rating: 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣")
        await message.channel.send(print_tally())

    elif message.content.startswith('+help'):
        await message.channel.send("Type +increment <number> to increase the tally of that number. Type +decrement <number> to decrease the tally of that number. Type +tally to see the current tally.")

    elif message.content.startswith("+tally"):
        await message.channel.send(print_tally())

    elif message.content.startswith('+increment'):
        if increment(message.content):
            await message.channel.send('Incremented!')
            await message.channel.send(print_tally())
        else:
            await message.channel.send('Can you repeat that? Type +help for more information.')

    elif message.content.startswith('+decrement'):
        if decrement(message.content):
            await message.channel.send('Decremented!')
            await message.channel.send(print_tally())
        else:
            await message.channel.send('Can you repeat that? Type +help for more information.')


client.run(token)
