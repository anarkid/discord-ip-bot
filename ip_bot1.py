import discord
from discord import Intents
import requests

TOKEN = 'xxxxxxx' # Make sure this is set
CHANNEL_ID = xxxxxxx # Replace with your channel ID

intents = Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

def get_public_ip():
    try:
        response = requests.get('https://api.myip.com', timeout=10)
        return response.json().get('ip', 'Unknown IP')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP: {e}")
        return "Unable to fetch IP"

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        ip_address = get_public_ip()
        await channel.send(f'The public IP address of the server is: {ip_address}')
        print(f'Sent IP address: {ip_address}')
    else:
        print(f'Channel with ID {CHANNEL_ID} not found.')

@client.event
async def on_connect():
    print('Bot connected to Discord!')

client.run(TOKEN)
