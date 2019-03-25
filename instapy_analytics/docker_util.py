import subprocess


def copy_database(container_name, database_path):
    subprocess.run([
        "docker",
        "cp",
        "{}:/root/InstaPy/db/instapy.db".format(container_name),
        database_path])
