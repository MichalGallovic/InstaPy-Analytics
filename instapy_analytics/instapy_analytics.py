from .instapy_db import InstapyDb
from .profile_activity import ProfileActivity
from .profile_progress import ProfileProgress
from .api_client import ApiClient


class InstapyAnalytics:
    def __init__(self,
                 username,
                 database_name,
                 host,
                 token):
        self.username = username

        if not username:
            raise Exception("Profile username is missing")

        if not database_name:
            raise Exception("Database path is missing")

        if not host:
            raise Exception("Analytics server host name is missing")

        if not token:
            raise Exception("Analytics server token is missing")

        self.db = InstapyDb(database_name)
        self.api_client = ApiClient(host, token)

    def send(self):
        profile_activity = self.get_profile_activity()
        profile_progress = self.get_profile_progress()

        profile_activity = list(map(lambda activity: activity.__dict__, profile_activity))
        profile_progress = list(map(lambda progress: progress.__dict__, profile_progress))

        self.api_client.send_profile_activity(profile_activity)
        self.api_client.send_profile_progress(profile_progress)

    def get_profile_activity(self):
        profile_activities = self.db.get_all_profile_activity(self.username)
        return list(map(lambda activity: ProfileActivity(self.username,
                                                      activity['likes'],
                                                      activity['comments'],
                                                      activity['follows'],
                                                      activity['unfollows'],
                                                      activity['server_calls'],
                                                      activity['created']), profile_activities))

    def get_profile_progress(self):
        profile_progress = self.db.get_all_profile_progress(self.username)
        return list(map(lambda progress: ProfileProgress(self.username,
                                                         progress['followers'],
                                                         progress['following'],
                                                         progress['total_posts'],
                                                         progress['created']), profile_progress))

