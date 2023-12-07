#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from web_static"""
import os
from fabric.api import local
import tarfile
from datetime import datetime


def do_pack():
    """generates a tgz archive"""
    try:
        n = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(
            n, "web_static/"))
        size = os.path.getsize("./versions/{}.tgz".format(n))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
            n, size))
    except:
        return None
