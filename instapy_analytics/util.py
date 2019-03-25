import os


def cleanup(database_path):
    if os.path.exists(database_path):
        os.remove(database_path)
    else:
        print("Db at location {} does not exist".format(database_path))
