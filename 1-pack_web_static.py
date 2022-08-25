#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


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
