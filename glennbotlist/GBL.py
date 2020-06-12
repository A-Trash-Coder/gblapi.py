import json
import aiohttp
import discord
from glennbotlist import errors
from glennbotlist.bot import Bot
from glennbotlist.user import User

class GBL:
    """
    API client for Glenn Bot List in Python

    Parameters
    ----------
    bot: `discord.ext.commands.Bot or discord.Client`
        A discord Bot or Client instance

    token: `Optional[str]`
        Your bots API key from Glenn Bot List

    logging: `boolean`
        Whether to have the glennbotlist client log for certain methods
    """

    def __init__(self, bot, token: str = None, logging: bool = False):
        self.bot = bot
        self.token = token
        self.logging = logging
        self.base = "https://glennbotlist.xyz/api/"
        self.session = aiohttp.ClientSession()

    async def request(self, method, url, headers={}, data={}):
        """This function is a coroutine

        Parameters
        ---------
        method: `str`
            The request method to use
        
        url: `str`
            The GBL path url

        headers: Optional[`dict`]
            Headers to pass to the request

        data: Optional[`dict`]
            Data to pass to the request
        """
        async with self.session.request(method=method, url=self.base + url, headers=headers, data=data) as r:
            resp = await r.json()
        
        if resp["code"] != 200:
            raise errors.HTTPException(f"An error occurred (HTTP Code {resp['code']})")

        return resp

    async def post_guild_count(self):
        """This function is a coroutine.

        Parameters
        ----------
        None

        Returns
        -------
        str
            Returns a success message

        Raises
        ------
        glennbotlist.NoKey
            Raised when self.token is None
        """
        if self.token is None:
            raise errors.NoKey("No API Key was passed")

        await self.request("POST", f"bot/{self.bot.user.id}/stats", data={"serverCount": len(self.bot.guilds), "shardCount": self.bot.shard_count or 0}, headers={"authorization": self.token})

        if self.logging:
            print(f"Your guild count of {len(self.bot.guilds)} and shard count of {self.bot.shard_count} was posted successfully")

    async def fetch_bot_stats(self, bot_id):
        """This function is a coroutine.

        Parameters
        ----------
        bot_id: `int`
            Bot to get info on

        Returns
        -------
        glennbotlist.Bot
            A Bot class
            
        Raises
        ------
        None
        """
        data = await self.request("GET", url=f"bot/{bot_id}/")

        return Bot(data=data)

    async def fetch_bot_votes(self):
        """This function is a coroutine.
        
        Requires authorization

        Parameters
        ----------
        None

        Returns
        -------
        dict
            Dictionary of bot votes

        Raises
        ------
        glennbotlist.Not200
            Http status code of the request was not 200
        """
        if self.token is None:
            raise errors.NoKey("No API Key was passed")

        data = await self.request("GET", url=f"bot/{self.bot.user.id}/votes", headers={"authorization": self.token})

        return data

    async def fetch_user_info(self, user_id: int):
        """This function is a coroutine.

        Parameters
        ----------
        user_id: `int`
            ID of the user you wish to get information on

        Returns
        ------
        dict
            Dictionary of user information

        Raises
        ------
        glennbotlist.Not200
            This is usually raised when the user is not registered on the list
        """
        data = await self.request("GET", url=f"user/{user_id}")

        return User(data=data)

    async def fetch_has_voted(self, user_id: int):
        """This function is a coroutine.

        Requires authorization

        Parameters
        ----------
        user_id: `int`
            ID of the user to get whether they have voted

        Returns
        ------
        boolean
            Whether the user has voted for the bot

        Raises
        ------
        glennbotlist.NoKey
            Raised when self.token is None
        """
        if self.token is None:
            raise errors.NoKey("No API Key was passed")

        resp = await self.request("GET", url=f"bot/{self.bot.user.id}/votes", headers={"authorization": self.token})

        current = resp['current_votes']['current_users']
        return str(user_id) in current

    async def fetch_vote_count(self):
        """This function is a coroutine.
        
        Requires authorization

        Parameters
        ----------
        None

        Returns
        -------
        int
            Amount of votes the bot has received

        Raises
        ------
        glennbotlist.NoKey
            Raised when self.token is None
        """

        if self.token is None:
            raise errors.NoKey("No API Key was passed")

        resp = await self.request("GET", url=f"bot/{self.bot.user.id}/votes", headers={"authorization": self.token})

        a = resp['current_votes']['alltime']
        m = len(resp['current_votes']['monthly'])

        return {"alltime": a, "monthly": m}