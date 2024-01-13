#!/usr/bin/python3
'''fabric;'''
from datetime import datetime
from fabric.api import *
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['52.3.243.233', '18.204.20.i81']

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
    '''deploying'''

    try:
        archive_path = 'versions/' + archive_path
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False

def deploy():
    '''deply'''

    archive_path = do_pack()
    return do_deploy(archive_path)
