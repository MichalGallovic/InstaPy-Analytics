#!/usr/bin/env python3
from instapy_analytics import InstapyAnalytics
from json import load
import optparse


def load_endpoints():
    with open("config.json") as f:
        config = load(f)
    f.close()

    if "endpoints" not in config:
        raise Exception("endpoints not configured in config.json")

    return config["endpoints"]

def main():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--username',
                      action='store', dest='username',
                      help='Define username')
    parser.add_option('-d', '--database',
                      action='store', dest='database_name',
                      help='Database name')
    parser.add_option('', '--host',
                      action='store', dest='host',
                      help='Analytics server host')
    parser.add_option('-t', '--token',
                      action='store', dest='token',
                      help='Analytics server api token')

    options, args = parser.parse_args()

    analytics = InstapyAnalytics(username=options.username,
                                 database_name=options.database_name,
                                 host=options.host,
                                 token=options.token,
                                 endpoints=load_endpoints())

    analytics.send()

    return None


if __name__ == '__main__':
    main()
