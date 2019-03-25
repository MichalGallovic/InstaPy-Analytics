class ProfileActivity:
    def __init__(self,
                 profile_name,
                 likes,
                 comments,
                 follows,
                 unfollows,
                 server_calls,
                 logged_at):
        self.profile_name = profile_name
        self.likes = likes
        self.comments = comments
        self.follows = follows
        self.unfollows = unfollows
        self.server_calls = server_calls
        self.logged_at = logged_at

    def __str__(self):
        return "Username: {}".format(self.profile_name) + \
                ", Likes: {}".format(self.likes) + \
                ', Comments: {}'.format(self.comments) + \
                ", Follows: {}".format(self.follows) + \
                ", Unfollows: {}".format(self.unfollows) + \
                ", Server calls: {}".format(self.server_calls) + \
                ", Logged at: {}".format(self.logged_at)
