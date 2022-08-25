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
        result = local(f"tar -czvf versions/web_static_{time}.tgz web_static")
        if result.succeeded:
            return (f"versions/web_static_{time}.tgz")
        else:
            return None
