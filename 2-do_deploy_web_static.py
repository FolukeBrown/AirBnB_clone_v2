#!/usr/bin/python3

"""
FABRIC script
"""
from fabric.api import run, put, env
import os

env.hosts = ['54.173.89.51', '54.85.26.50']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    # Uploading archive
    try:
        # removing parent directory version/ from file name
        file = archive_path.split("/")[-1]
        # removing extension
        file_no_ext = file.split(".")[0]
        server_path = "/data/web_static/releases/{}/".format(file_no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(server_path))
        # Uncompressing the archive into the created directory
        run("tar -xzf /tmp/{} -C {}".format(file, server_path))
        # Deleting the archive
        run("rm /tmp/{}".format(file))
        # Changing directory
        run("mv {}web_static/* {}".format(server_path, server_path))
        run("rm -rf {}web_static".format(server_path))
        # Deleting symbolic link
        run("rm -rf {}".format(symlink))
        # New symbolic link
        run("ln -s {} {}".format(server_path, symlink))
        return True
    except Exception:
        return False
