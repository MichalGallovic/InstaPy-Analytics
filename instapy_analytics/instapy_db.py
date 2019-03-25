import sqlite3
import os


class InstapyDb:
    def __init__(self, database_path):

        if not os.path.isfile(database_path):
            raise Exception("There is no database at {}".format(database_path))

        if not database_path.endswith(".db"):
            raise Exception("Database file must end with .db")

        self.database_path = database_path
        self.connection = None

    def get_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.database_path)
        return self.connection

    def fetch_all(self, sql, parameters):
        connection = self.get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        return cursor.fetchall()

    def get_all_profile_activity(self, username):
        sql = "select * from recordActivity " \
              "join profiles on profiles.id = recordActivity.profile_id " \
              "where profiles.name = :username"

        return self.fetch_all(sql, {'username': username})

    def get_all_profile_progress(self, profile_name):
        sql = "select * from accountsProgress " \
              "join profiles on profiles.id = accountsProgress.profile_id " \
              "where profiles.name = :username"

        return self.fetch_all(sql, {'username': profile_name})
