class Bot:
    """Represents a bot listed on Glenn Bot List.

    Operations
    ----------
    x == y
        Checks if two bot's are the same.

    x != y
        Checks if two bot's are not the same.
    
    str(x)
        Returns the bot's name.

    Attributes
    ---------
    name: `str`
        The bot's name
    
    id: `int`
        The bot's ID
    
    main_owner: `int`
        The ID of the bot's main owner
    
    owners: `list`
        Alternate owners of the bot

    library: `str`
        Library the bot is coded in

    monthly_upvotes: `list`
        List of votes the bot has received for the month

    total_upvotes: `int`
        Amount of votes the bot has received since being on the list

    website: `str`
        Bot's website

    github: `str`
        Bot's GitHub

    short_description: `str`
        Short description of the bot

    prefix: `str`
        Bot's prefix
    
    partnered: `boolean`
        Whether the bot is partnered with Glenn Bot List

    vanity_url: `str` 
        Bot's website vanity URL

    featured: `boolean`
        Whether the bot is currently featured

    invite_url: `str`
        Invite url for the bot

    server_count: `int`
        Bot's server count

    shard_count: `int`
        Bot's shard count
    
    tags: `list`
        The tags associated with the bot

    rates: `list`
        List of the bot's rates
    """
    def __init__(self, data):
        self.name = data["name"]
        self.id = int(data["id"])
        self.main_owner = int(data["main_owner"])
        self.owners = data["owners"]
        self.library = data["library"]
        self.monthly_upvotes = ["monthly_upvotes"]
        self.total_upvotes = int(data["total_upvotes"])
        self.website = data["website"]
        self.github = data["github"]
        self.short_description = data["short_description"]
        self.prefix = data["prefix"]
        self.partnered = data["partnered"]
        self.vanity_url = data["vanity_url"]
        self.featured = data["featured"]
        self.invite_url = data["invite_url"]
        self.server_count = int(data["server_count"])
        self.shard_count = int(data["shard_count"])
        self.tags = data["tags"]
        self.rates = data["rates"]

    def __eq__(self, other_bot):
        return isinstance(other_bot, Bot) and other_bot.id == self.id

    def __ne__(self, other_bot):
        return not self.__eq__(other_bot)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Bot id: {0.id} name: '{0.name}' main_owner: '{0.main_owner}' prefix: {0.prefix}>".format(self)
