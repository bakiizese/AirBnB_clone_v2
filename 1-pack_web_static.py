#!/usr/bin/python3
'''fabric;'''
from datetime import datetime
from fabric.api import *


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
