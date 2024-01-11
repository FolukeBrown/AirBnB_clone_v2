#!/usr/bin/python3

"""
A Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from time import strftime


def do_pack():
    """
    Archives the files in the web static directory.
    The archived files are saved in the version directory.
    """
    # Create /version directory if not exists.
    local('mkdir -p versions')

    # Archiving
    _time = strftime("%Y%M%d%H%M%S")
    try:
        local("tar -czvf versions/web_static_{}.tgz  web_static/"
              .format(_time))
        return "versions/web_static_{}.tgz".format(_time)
    except Exception:
        return None
