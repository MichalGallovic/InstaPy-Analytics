#!/usr/bin/env python3
from instapy_analytics import InstapyAnalytics
import optparse


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
                                 token=options.token)

    analytics.send()

    return None


if __name__ == '__main__':
    main()
