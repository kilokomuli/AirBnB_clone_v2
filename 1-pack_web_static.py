#!/usr/bin/python3
""" Generates a tgz archive from the contents
of web static folder"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    try:
        now = datetime.now()
        name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                    now.day, now.hour,
                                                    now.minute, now.second)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
