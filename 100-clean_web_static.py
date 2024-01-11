#!/usr/bin/python3

"""
A script that deletes out_of_date archives
"""
from fabric.api import local, run, env

env.hosts = ['54.173.89.51', '54.85.26.50']


def do_clean(number=0):
    """
    Delete archives
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    for arch in range(number):
        archives.pop()

    with lcd("versions"):
        for arch in archives:
            local("rm ./{}".format(arch))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        arch = [arc for arc in archives if "web_static_" in arc]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(arc)) for arc in arch]
