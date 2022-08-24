#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local
from datetime import datetime

def do_pack():
    """ The function do_pack """
    local("mkdir -p versions")
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    file = f"versions/web_static_{time}.tgz"

    try:
        local(f"tar -czvf {file} web_static")
        return file

    except Exception:
        return None
