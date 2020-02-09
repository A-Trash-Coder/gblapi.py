# GBLPYAPI
The official API wrapper for glennbotlist.xyz in Python

[Glenn Bot List](https://glennbotlist.xyz)

[Pypi](https://pypi.org/project/gblpyapi/)

## Installation
``pip install gblpyapi``

## Features
Funtion  | Action
------------- | -------------
post_server_count(botid, guilds)  | POST Server Count

# Examples
## Post server count

```python
import discord
import glennbotlist.GBL as GBL
from discord.ext import tasks

gbl = GBL.GBL(token) # glenbotlist.xyz API token

@tasks.loop(minutes = 30) # Posts server count every 30 minutes
async def postservers(self):
    await self.gbl.post_server_count(self.bot.user.id, len(self.bot.guilds))

```


