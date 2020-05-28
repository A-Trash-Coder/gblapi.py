class User:
    """Represents a bot listed on Glenn User List.

    Operations
    ----------
    x == y
        Checks if two user's are the same.

    x != y
        Checks if two user's are not the same.
    
    str(x)
        Returns the user's name and discriminator.

    Attributes
    ---------
    id: `int`
        The user's ID
    
    name: `str`
        The user's name
    
    discriminator: `str`
        The user's 4 digit discriminator
    
    avatar: `str`
        The user's avatar url
    
    bio: `str`
        The user's bio
    
    custom_background: `str`
        Whether the user has a cutsom background
    
    mod: `str`
        Whether the user is a GBL Moderator
    
    admin: `str`
        Whether the user is a GBL Admin

    karma: `int`
        Karma the user's collected for the current month

    total_karma: `int`
        Total amount of karma the users collected
    """
    def __init__(self, data):
        self.id = int(data["id"])
        self.name = data["username"]
        self.discriminator = data["discriminator"]
        self.avatar = data["avatar"]
        self.bio = data["bio"]
        self.custom_background = data["custom_background"]
        self.mod = data["mod"]
        self.admin = data["admin"]
        self.karma = int(data["karma"])
        self.total_karma = int(data["total_karma"])

    def __eq__(self, other_user):
        return isinstance(other_user, User) and other_user.id == self.id

    def __ne__(self, other_user):
        return not self.__eq__(other_user)

    def __str__(self):
        return self.name + "#" + self.discriminator

    def __repr__(self):
        return "<User id: {0.id} name: '{0.name}' discriminator: '{0.discriminator}' mod: {0.mod}>".format(self)