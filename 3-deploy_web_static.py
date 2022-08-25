#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your
web servers, using the function deploy
"""

from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists

env.hosts = ['23.20.75.80', '54.83.87.163']


def do_pack():
    """
    Generates a .tgz archive from the contents
    of the web_static folder of the AirBnB Clone repo
    """

    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -czvf versions/web_static_{}.tgz \
        web_static".format(time))
    if result.succeeded:
        return ("versions/web_static_{}.tgz".format(time))
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """

    if exists(archive_path):
        filename = archive_path.split("/")[-1]
        filename_noext = filename.split(".")[0]
        put(archive_path, "/tmp/")
        r1 = run("mkdir -p /data/web_static/releases/\
{}".format(filename_noext))
        r2 = run("tar -xzf /tmp/{} -C /data/web_static/releases/\
{}/".format(filename, filename_noext))
        r3 = run("rm /tmp/{}".format(filename))
        r4 = run("mv /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/".format(filename_noext, filename_noext))
        r5 = run("rm -rf /data/web_static/releases/\
{}/web_static".format(filename_noext))
        r6 = run("rm -rf /data/web_static/current")
        r7 = run("ln -s /data/web_static/releases/{}/\
 /data/web_static/current".format(filename_noext))
        if (r1.failed or r2.failed or r3.failed or r4.failed or
                r5.failed or r6.failed or r7.failed):
            return False
    else:
        return True


def deploy():
    """
    Creates and distributes an archive to your web servers
    """

    path = do_pack()
    if path is not None:
        status = do_deploy(path)
        return status
    else:
        return False
