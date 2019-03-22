import requests


class ApiClient:
    PROFILES_ACTIVITY = '/profiles/activity'
    PROFILES_PROGRESS = '/profiles/progress'

    def __init__(self, host, token):
        self.host = host
        self.token = token

    def __create_token_header(self):
        return {'X-Request-Token': self.token}

    def __create_url(self, resource):
        return "{}/api/{}".format(self.host, resource)

    def __post(self, url, data):
        response = requests.post(url, json=data, headers=self.__create_token_header())
        response.raise_for_status()
        return response.json()

    def send_profile_activity(self, activity):
        self.__post(self.__create_url(self.PROFILES_ACTIVITY), activity)

    def send_profile_progress(self, progress):
        self.__post(self.__create_url(self.PROFILES_PROGRESS), progress)