# gblapi.py - The official Python API Wrapper for the GBL API

![PyPI](https://img.shields.io/pypi/v/gblpyapi?logoColor=237289DA)

# About
This is the **official** API wrapper for GlennBotList.xyz written in Python and published to [PyPi](https://pypi.org/project/gblpyapi/).

# Installation
To install **gblapi.py**, run this command in a terminal:

> $ pip install gblpyapi

## Features

|Method|Action|
|--------|------|
|`post_guild_count(bot_id, guild_count, shard_count: optional)` (note: requires authentication)|POST guild count|
|`fetch_user_info(user_id)`|GET user info|
|`fetch_has_voted(user_id)` (note: required authentication)|GET if a user has voted|
|`fetch_bot_votes(bot_id)` (note: requires authentication)|GET bot votes|
|`fetch_bot_stats(bot_id)`|GET bot stats|
|`fetch_vote_count(bot_id)`|GET bot vote count|

# Examples

## Post server count

```python
from glennbotlist import GBL
from discord.ext import tasks

gbl = GBL("token") # glenbotlist.xyz API token

@tasks.loop(minutes=30) # posts guild count every 30 minutes
async def post_guilds(self):
    await gbl.post_guild_count(self.bot.user.id, len(self.bot.guilds))
```

## Get Bot Info

```python
import discord
from glennbotlist import GBL
from discord.ext import commands

gbl = GBL()

@commands.command()
async def botinfo(self, ctx, user: discord.Member):
    if not user.bot:
        await ctx.send("This user is not a bot!")
        return

    info = await gbl.fetch_bot_stats(user.id)
    await ctx.send(info['name'])
```

## Get Bot Votes

```python
from glennbotlist import GBL
from discord.ext import commands

gbl = GBL("token") # glenbotlist.xyz API token

@commands.command()
async def botvotes(self, ctx):
    votes = await gbl.fetch_bot_votes(self.bot.user.id)
    await ctx.send(votes['current_votes']['monthly']) # people who have voted this month
```

## Get Bot Vote Count

```python
from glennbotlist import GBL
from discord.ext import commands

gbl = GBL("token") # glenbotlist.xyz API token

@commands.command()
async def botvotecount(self, ctx):
    votes = await gbl.fetch_vote_count(self.bot.user.id)
    await ctx.send(votes['alltime']) # all time votes
```

## Get User Info

```python
import discord
from glennbotlist import GBL
from discord.ext import commands

gbl = GBL()

@commands.command()
async def userinfo(self, ctx, user: discord.Member):
    info = await gbl.fetch_user_info(user.id)
    await ctx.send(info['username'])
```

## Get User Has Voted

```python
import discord
from glennbotlist import GBL
from discord.ext import commands

gbl = GBL("token") # glenbotlist.xyz API token

@commands.command()
async def voted(self, ctx, user: discord.Member):
    if user.bot:
        await ctx.send("This user is a bot!")
        return

    voted = await gbl.fetch_has_voted(self.bot.id, user.id)
    await ctx.send(voted)
```

# Authors

Made with ❤️ by A Trash Coder#0981 and A Discord User#6130.

# Help

Join the [Discord](https://glennbotlist.xyz/discord) for more help on this module.