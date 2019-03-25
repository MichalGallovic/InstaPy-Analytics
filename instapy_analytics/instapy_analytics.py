from .instapy_db import InstapyDb
from .profile_activity import ProfileActivity
from .profile_progress import ProfileProgress
from .api_client import ApiClient


class InstapyAnalytics:
    def __init__(self,
                 profile_name,
                 database_name,
                 host,
                 token,
                 endpoints):
        self.profile_name = profile_name

        if not profile_name:
            raise Exception("Profile name is missing")

        if not database_name:
            raise Exception("Database path is missing")

        if not host:
            raise Exception("Analytics server host name is missing")

        self.db = InstapyDb(database_name)
        self.api_client = ApiClient(host, token, endpoints)

    def send(self):
        profile_activities = self.get_profile_activities()
        profile_progress = self.get_profile_progress()

        profile_activities = list(map(lambda activity: activity.__dict__, profile_activities))
        profile_progress = list(map(lambda progress: progress.__dict__, profile_progress))

        if profile_activities:
            self.api_client.send_profile_activity(profile_activities)

        if profile_progress:
            self.api_client.send_profile_progress(profile_progress)

    def get_profile_activities(self):
        profile_activities = self.db.get_all_profile_activity(self.profile_name)

        if not profile_activities:
            print("There are no profile activity records for profile {} in recordActivity table".format(self.profile_name))

        return list(map(lambda activity: ProfileActivity(self.profile_name,
                                                      activity['likes'],
                                                      activity['comments'],
                                                      activity['follows'],
                                                      activity['unfollows'],
                                                      activity['server_calls'],
                                                      activity['created']), profile_activities))

    def get_profile_progress(self):
        profile_progress = self.db.get_all_profile_progress(self.profile_name)

        if not profile_progress:
            print("There are no profile progress records for profile {} in accountsProgress table".format(self.profile_name))

        return list(map(lambda progress: ProfileProgress(self.profile_name,
                                                         progress['followers'],
                                                         progress['following'],
                                                         progress['total_posts'],
                                                         progress['created']), profile_progress))

