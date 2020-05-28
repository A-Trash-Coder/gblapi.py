# gblapi.py - The official Python API Wrapper for the GBL API

![PyPI](https://img.shields.io/pypi/v/gblpyapi?logoColor=237289DA)

# About
This is the **official** API wrapper for GlennBotList.xyz written in Python and published to [PyPi](https://pypi.org/project/gblpyapi/).

# Installation
To install **gblapi.py**, run this command in a terminal:

> $ pip install gblpyapi

# Features

## glennbotlist.WebhookServer

gblpyapi now has a webhook server! Create an instance of the WebhookServer module and pass the required parameters. Get when a user votes with the event below!

|Event Name|Parameters|
|--------|------|
|`on_glenn_vote`|data|

## glennbotlist.GBL

|Method|Action|
|--------|------|
|`post_guild_count()` (note: requires authentication)|POST guild count|
|`fetch_user_info(user_id)`|GET user info|
|`fetch_has_voted(user_id)` (note: required authentication)|GET if a user has voted|
|`fetch_bot_votes()` (note: requires authentication)|GET bot votes|
|`fetch_bot_stats(bot_id)`|GET bot stats|
|`fetch_vote_count()` (note: requires authentication)|GET bot vote count|

# Examples

To easily combine all examples, all examples will be shown in a discord.ext.commands.Cog

```python
from glennbotlist import GBL
from glennbotlist import WebhookServer
import discord
from discord.ext import commands, tasks

class GlennBotList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.glenn = GBL(bot=self.bot, token=config.gbl, logging=True) # Replace "GBL TOKEN" with your GBL Token. True enables logging.
        self.server = WebhookServer(self.bot) # Initiate Webhook Server
        self.postservers.start() # Starts the postservers task

    @commands.Cog.listener()
    async def on_glenn_vote(self, data): # Triggered whenever a user votes
        print(data)

    @tasks.loop(hours = 1)
    async def postservers(self):
        await self.glenn.post_guild_count() # Post you server count and shard count. If logging is enabled, it will print a success message

    @commands.command()
    async def user_info(self, ctx, user: discord.Member):
        if user.bot:
            return await ctx.send("This user is not a bot")
        
        guser = await self.glenn.fetch_user_info(user.id) # Returns a glennbotlist.User object
        await ctx.send(f"Name: {guser.name}. Bio: {guser.bio}") # Sends the users name and bio. For all User attributes, print the directory of glennbotlist.User

    @commands.command()
    async def has_voted(self, ctx, user: discord.Member):
        if user.bot:
            return await ctx.send("This user is not a bot")
        
        voted = await self.glenn.fetch_has_voted(user.id) # Returns a bool of whether the user has voted
        await ctx.send(f"{user}'s vote status: {voted}")

    @commands.command()
    async def votes(self, ctx):
        votes = await self.glenn.fetch_bot_votes() # Gets a dict of votes
        await ctx.send(votes)
        
    @commands.command()
    async def botinfo(self, ctx, user: discord.Member):
        if not user.bot:
            await ctx.send("This is not a bot!")

        bot = await self.glenn.fetch_bot_stats(user.id) # Returns a glennbotlist.Bot object
        await ctx.send(f"Name: {bot.name}. Prefix: {bot.prefix}") # Sends the bots name and prefix. For all Bot attributes, print the directory of glennbotlist.Bot

    @commands.command()
    async def vote_count(self, ctx):
        votes = await self.glenn.fetch_vote_count() # Gets all time and monthly votes
        await ctx.send(f"I have {votes['monthly']} votes this month!") # Sends amount of votes for the current month

def setup(bot):
    bot.add_cog(GlennBotList(bot))
```

# Authors

Made with ❤️ by A Trash Coder#0214 and A Discord User#1173.

# Help

Join the [Discord](https://glennbotlist.xyz/discord) for more help on this module.