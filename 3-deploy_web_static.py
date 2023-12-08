#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from web_static"""
import os
from fabric.api import local, env, run, put
import tarfile
from datetime import datetime


env.hosts = ['100.25.15.101', '18.234.107.33']
env.user = 'ubuntu'


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

def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    f = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/{}'.format(f))
        run('mkdir -p /data/web_static/releases/{}'.format(f))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(f, f))
        run('rm /tmp/{}'.format(f))
        run('mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/'.format(f, f))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(f))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/\
        /data/web_static/current'.format(f))
        print("New version deployed!")
        return True
    except:
        print("New version not deployed...")
        return False

def deploy():
    """creates and distributes an archive to your web servers"""
    ap = do_pack()
    if ap is None:
        return False
    return do_deploy(ap)
