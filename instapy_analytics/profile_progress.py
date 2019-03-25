class ProfileProgress:
    def __init__(self,
                 profile_name,
                 followers,
                 following,
                 total_posts,
                 logged_at):
        self.profile_name = profile_name
        self.followers = followers
        self.following = following
        self.total_posts = total_posts
        self.logged_at = logged_at

    def __str__(self):
        return "Username: {}".format(self.profile_name) + \
            ", Followers: {}".format(self.followers) + \
            ", Following: {}".format(self.following) + \
            ", Total posts: {}".format(self.total_posts) + \
            ", Logged at: {}".format(self.logged_at)
