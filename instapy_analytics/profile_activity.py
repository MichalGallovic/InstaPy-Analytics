class ProfileActivity:
    def __init__(self,
                 username,
                 likes,
                 comments,
                 follows,
                 unfollows,
                 server_calls,
                 created):
        self.username = username
        self.likes = likes
        self.comments = comments
        self.follows = follows
        self.unfollows = unfollows
        self.server_calls = server_calls
        self.created = created

    def __str__(self):
        return "Username: {}".format(self.username) + \
                ", Likes: {}".format(self.likes) + \
                ', Comments: {}'.format(self.comments) + \
                ", Follows: {}".format(self.follows) + \
                ", Unfollows: {}".format(self.unfollows) + \
                ", Server calls: {}".format(self.server_calls) + \
                ", Created at: {}".format(self.created)
