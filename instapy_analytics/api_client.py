import requests


class ApiClient:

    PROFILE_ACTIVITY = 'profile_activity'
    PROFILE_PROGRESS = 'profile_progress'

    def __init__(self, host, token, endpoints):
        self.host = host
        self.token = token
        self.endpoints = endpoints

    def __create_resource(self, resource_key):
        if resource_key not in self.endpoints:
            raise Exception("{} is not defined in config.json".format(resource_key))

        if not self.endpoints[resource_key]:
            raise Exception("{} is empty".format(resource_key))

        return self.endpoints[resource_key]

    def __create_url(self, resource_key):
        resource = self.__create_resource(resource_key)
        return "{}{}".format(self.host, resource)

    def __create_data(self, data):
        return {
            "data": data
        }

    def __post(self, url, data):
        data = self.__create_data(data)

        if self.token:
            data['api_token'] = self.token

        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def send_profile_activity(self, activity):
        self.__post(self.__create_url(self.PROFILE_ACTIVITY), activity)

    def send_profile_progress(self, progress):
        self.__post(self.__create_url(self.PROFILE_PROGRESS), progress)
