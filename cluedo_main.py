import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.dm_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

#global variables
global solution
global player
solution = 0
player=[0]

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


@bot.command(name='get_answer')
async def get_answer(ctx):
  if not isinstance(ctx.channel, discord.channel.DMChannel):
    await ctx.send(f'||{solution}||')
  else:
    await ctx.send('You cheater...')
  return

@bot.command(name='clue_send')
async def clue_send(ctx, user: discord.User, *, message):
  message = message or "This Message is sent via DM"
  await user.send(message)


@bot.command(name='cluedo')
async def play(ctx, *players: discord.Member):
  if not 2 <= len(players) <= 4:
    await ctx.send("Please provide 2 to 4 players.")
    return

  # Create decks
  locations = ['Dining Room', 'Living Room', 'Hall', 'Kitchen', 'Spa']

  weapons = ['Candlestick', 'Knife', 'Rope', 'Pistol']

  suspects = ['Scarlett', 'Mustard', 'Green', 'Peacock', 'Plum', 'White']

  # Shuffle decks
  random.shuffle(locations)
  random.shuffle(weapons)
  random.shuffle(suspects)

  # Send the solution in the channel
  solution_location = random.choice(locations)
  solution_weapon = random.choice(weapons)
  solution_suspect = random.choice(suspects)
  solution = 'Solution: ' + f'{solution_location}, {solution_weapon}, {solution_suspect}'

  # Gather all cards and remove selected ones
  total_cards = locations + weapons + suspects
  total_cards.remove(solution_location)
  total_cards.remove(solution_weapon)
  total_cards.remove(solution_suspect)
  random.shuffle(total_cards)

  # Math for how many cards to send
  number_total_cards = len(total_cards)
  total_players = len(players)
  cards_per_player = number_total_cards // total_players
  extra_cards = number_total_cards % total_players
  player_hand = []

  # Send cards via DM
  for p in players:
    #await ctx.send(f'{p}')
    
    player_hand = (total_cards[:(cards_per_player)])
    total_cards = total_cards[(cards_per_player):]

    if extra_cards > 0:
      player_hand.append(total_cards[0])
      total_cards = total_cards[1:]
      extra_cards -= 1

    await p.send(f'Your Cluedo Cards:\n{", ".join(player_hand)}')

  await ctx.send(f'The cards have been sent to {total_players} players.')


#Token
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  bot.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e