import discord
import magic_items as mi
import roller as r

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

FOLDER_PATH = '/home/hammy2015/mysite/attrpgb'

key = open(FOLDER_PATH + "/disckey.txt","r")

keystring = key.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!attrpgb'):
        await message.channel.send('Hello! This is the attrpgb bot. How can I assist you today?')

    # Magic item generator logic, uses logic determined here: https://www.d20pfsrd.com/magic-items/wondrous-items/
    if message.content.startswith('!mig'):
        price = int(message.content.split()[-1])
        tier = message.content.split()[-2]
        print(message.content.split()[-1] + ' ' + tier)
        if tier == '$mig':
            item = mi.mig(price)
        else:
            item = mi.mig(price,tier)
        await message.channel.send(item)

    # Dice rolling logic, real basic for now
    if message.content.startswith('!roll'):
        dice_sides = int(message.content.split()[1].split('d')[1])
        num_dice = int(message.content.split()[1].split('d')[0])
        if message.content.contains('+'):
            roll_mod = int(message.content.split('+')[1])
        elif message.content.contains('-'):
            roll_mod = -int(message.content.split('-')[1])

    # TODO: profession rules for making money https://www.d20pfsrd.com/skills/profession/
    if message.content.startswith('!prof'):
        days = message.content.split()[1]
        skill = message.content.split()[2]
        total = 0
        for x in range(0, int(days)):
            total = total + r.roll_dice_with_advantage(1, 20, True) + int(skill)

        await message.channel.send(f'You made {total} gp in {days} days of work.')

    # TODO: 
        

client.run(keystring)