import requests
import json
import aiohttp

from . import errors

class GBL:
    """
    API client for Glenn Bot List in Python
    """
    def __init__(self, token: str, *, base: str = "https://glennbotlist.xyz/api/v2/bot/"):
        self.token = token
        self.base = base
        self.session = aiohttp.ClientSession()

    async def post_server_count(self, botid: int, servers: int):
        """

        :param botid: Bot ID in which you are posting the stats for
        :param servers: The bots server coint
        """
        if not self.token:
            raise errors.InvalidKey("A token was not supplied")

        async with self.session.post(url=self.base + f"{botid}/stats", data={"serverCount": servers}, headers={"authorization": self.token}) as r:
            resp = await r.json()
        
        if resp['code'] != 200:
            raise errors.InvalidKey("You're token was incorrect or another error has occured")
        else:
            print(f"Your server count of {servers} was posted successfully (Code: 200)")