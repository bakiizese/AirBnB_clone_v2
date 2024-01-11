#!/usr/bin/python3
'''fabric;'''
from datetime import datetime
from fabric.api import *
from os.path import exists
env.host = ['52.3.243.233', '18.204.20.81']

def do_pack():
    """do packing"""

    tm = datetime.now()
    arch = 'web_static_' + tm.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    lc = local('tar -cvzf versions/{} web_static'.format(arch))
    if lc is not None:
        return arch
    else:
        return None

def do_deploy(archive_path):
    '''deploying in server'''

    if exists(archive_path) is False:
        return False
    try:
        fl = archive_path.split("/")[-1]
        tx = fl.split(".")[0]
        ph = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(ph, tx))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fl, ph, tx))
        run('rm /tmp/{}'.format(fl))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(ph, tx))
        run('rm -rf {}{}/web_static'.format(ph, tx))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(ph, tx))
        return True
    except:
        return False
