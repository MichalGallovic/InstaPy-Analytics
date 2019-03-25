#!/usr/bin/env python3
from instapy_analytics import InstapyAnalytics
from json import load
import optparse
from instapy_analytics import copy_database
from instapy_analytics import cleanup


def load_endpoints():
    with open("config.json") as f:
        config = load(f)
    f.close()

    if "endpoints" not in config:
        raise Exception("endpoints not configured in config.json")

    return config["endpoints"]

def main():
    parser = optparse.OptionParser()
    parser.add_option('-p', '--profile_name',
                      action='store', dest='profile_name',
                      help='Define profile name')
    parser.add_option('-d', '--database_path',
                      action='store', dest='database_path',
                      help='Database path')
    parser.add_option('', '--host',
                      action='store', dest='host',
                      help='Analytics server host')
    parser.add_option('-t', '--token',
                      action='store', dest='token',
                      help='Analytics server api token')

    parser.add_option('-c', '--container_name',
                      action='store', dest='container_name',
                      help='Docker container name')

    options, args = parser.parse_args()

    if not options.profile_name:
        raise Exception("Profile name is missing")

    if not options.database_path:
        raise Exception("Database path is missing")

    if not options.host:
        raise Exception("Analytics server host name is missing")

    if options.container_name:
        copy_database(options.container_name, options.database_path)

    analytics = InstapyAnalytics(profile_name=options.profile_name,
                                 database_path=options.database_path,
                                 host=options.host,
                                 token=options.token,
                                 endpoints=load_endpoints())

    analytics.send()

    return None


if __name__ == '__main__':
    main()
