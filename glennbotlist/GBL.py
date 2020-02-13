import requests
import json
import aiohttp

from . import errors

class GBL:
    """
    API client for Glenn Bot List in Python
    """
    def __init__(self, token: str=None, *, base: str = "https://glennbotlist.xyz/api/v2/"):
        self.token = token
        self.base = base
        self.session = aiohttp.ClientSession()

    async def post_server_count(self, botid: int, servers: int):
        """This function is a coroutine.

        POST bots stats
        
        Requires authorization

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.post(url=self.base + f"bot/{botid}/stats", data={"serverCount": servers}, headers={"authorization": self.token}) as r:
            resp = await r.json()
        
        if resp['code'] != 200:
            raise errors.Not200(f"Your token was incorrect or another error has occured (Code {resp['code']})")
        else:
            print(f"Your server count of {servers} was posted successfully (Code: 200)")

    async def get_bot_stats(self, botid: int):
        """This function is a coroutine.

        GET bots stats

        Returns
        =======

        bot stats: json
            List of bot stats

        """
        async with self.session.get(url=self.base + f"bot/{botid}") as r:
            resp = await r.json()
            if resp['code'] != 200:
                raise errors.Not200(f"The bot id is incorrect or another error has occured (Code {resp['code']})")
            else:
                return resp

    async def get_bot_votes(self, botid: int):
        """This function is a coroutine.

        GET bots votes
        
        Requires authorization

        Returns
        =======

        bot votes: json
            List of bot votes

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.get(url=self.base + f"bot/{botid}/votes", headers={"authorization": self.token}) as r:
            resp = await r.json()
            if resp['code'] != 200:
                raise errors.Not200(f"The bot id or token is incorrect or another error has occured (Code {resp['code']})")
            else:
                return resp

    async def get_user_info(self, userid: int):
        """This function is a coroutine.

        GET user's info

        Returns
        =======

        bot info: json
            List of info

        """
        async with self.session.get(url=self.base + f"profile/{userid}") as r:
            resp = await r.json()
            if resp['code'] != 200:
                raise errors.Not200(f"The user id is incorrect or another error has occured (Code {resp['code']})")
            else:
                return resp

    async def get_has_voted(self, botid: int, userid: int):
        """This function is a coroutine.

        GET wether a user has voted or not
        
        Requires authorization

        Returns
        =======

        users vote: Boolean

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.get(url=self.base + f"bot/{botid}/votes", headers={"authorization": self.token}) as r:
            resp = await r.json()
            if resp['code'] != 200:
                raise errors.Not200(f"The bot id or token is incorrect or another error has occured (Code {resp['code']})")
            else:
                current = resp['current_votes']['current_users']
                return f"{userid}" in current