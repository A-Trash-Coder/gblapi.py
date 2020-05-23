import json
import aiohttp

from glennbotlist import errors

class GBL:
    """
    API client for Glenn Bot List in Python
    """

    def __init__(self, token: str = None, *, base: str = "https://glennbotlist.xyz/api/"):
        self.token = token
        self.base = base
        self.session = aiohttp.ClientSession()

    async def post_guild_count(self, bot_id: int, guild_count: int, shard_count: int = None):
        """This function is a coroutine.

        POST bot stats

        Requires authorization

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.post(url=self.base + f"bot/{bot_id}/stats", data={"serverCount": guild_count, "shardCount": shard_count or 0}, headers={"authorization": self.token}) as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"Your token was incorrect or another error has occurred (Code {resp['code']})")

        print(f"Your guild count of {guild_count} was posted successfully (Code: 200)")

    async def fetch_bot_stats(self, bot_id: int):
        """This function is a coroutine.

        GET bot stats

        Returns
        =======

        bot stats: dict
            List of bot stats

        """
        async with self.session.get(url=self.base + f"bot/{bot_id}/") as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"The bot id is incorrect or another error has occurred (Code {resp['code']})")

        return resp

    async def fetch_bot_votes(self, bot_id: int):
        """This function is a coroutine.

        GET bot votes
        
        Requires authorization

        Returns
        =======

        bot votes: dict
            List of bot votes

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.get(url=self.base + f"bot/{bot_id}/votes", headers={"authorization": self.token}) as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"The bot id or token is incorrect or another error has occured (Code {resp['code']})")

        return resp

    async def fetch_user_info(self, user_id: int):
        """This function is a coroutine.

        GET user's info

        Returns
        =======

        bot info: json
            List of info

        """
        async with self.session.get(url=self.base + f"user/{user_id}") as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"The user id is incorrect or another error has occurred (Code {resp['code']})")

        return resp

    async def fetch_has_voted(self, bot_id: int, user_id: int):
        """This function is a coroutine.

        GET whether a user has voted or not

        Requires authorization

        Returns
        =======

        users vote: Boolean

        """
        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.get(url=self.base + f"bot/{bot_id}/votes", headers={"authorization": self.token}) as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"The bot id or token is incorrect or another error has occured (Code {resp['code']})")

        current = resp['current_votes']['current_users']
        return str(user_id) in current

    async def fetch_vote_count(self, bot_id: int):
        """This function is a coroutine.

        GET vote count
        
        Requires authorization

        Returns
        =======

        votes: integer

        """

        if self.token is None:
            raise errors.NoKey("A token was not supplied")

        async with self.session.get(url=self.base + f"bot/{bot_id}/votes", headers={"authorization": self.token}) as r:
            resp = await r.json()

        if resp['code'] != 200:
            raise errors.Not200(f"The bot id or token is incorrect or another error has occured (Code {resp['code']})")

        a = resp['current_votes']['alltime']
        m = len(resp['current_votes']['monthly'])

        return {"alltime": a, "monthly": m}