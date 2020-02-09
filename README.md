# gblapi.py - The official PY API Wrapper for the GBL API

# About
This is the **official** api wrapper for GlennBotList.xyz written in PY, and published to [Pypi](https://pypi.org/project/gblpyapi/)

# Installation
To install **gblapi.py** run this command in a terminal:

> Install gblapi.py:
>
>```
>pip install gblpyapi
>```

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

# Authors
> Made by `CoderLamar420#0981`

# Help
> Join our [Discord Server](https://glennbotlist.xyz/discord) for help on this module.


