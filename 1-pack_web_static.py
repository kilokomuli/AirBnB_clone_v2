#!/usr/bin/python3
""" Generates a tgz archive from the contents
of web static folder"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    name = "versions/web_static_{}.tgz".format(now)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(name))
        return name
    except:
        return None
