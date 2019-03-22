class ProfileProgress:
    def __init__(self,
                 username,
                 followers,
                 following,
                 total_posts,
                 created):
        self.username = username
        self.followers = followers
        self.following = following
        self.total_posts = total_posts
        self.created = created

    def __str__(self):
        return "Username: {}".format(self.username) + \
            ", Followers: {}".format(self.followers) + \
            ", Following: {}".format(self.following) + \
            ", Total posts: {}".format(self.total_posts) + \
            ", Created: {}".format(self.created)
