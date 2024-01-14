#!/usr/bin/python3
"""
This is the 2-do_deploy_web_static.py module.
This module distribute the static content (html, css, images) to the servers
"""


from fabric.api import put, run, env, task
import os
env.hosts = ['52.3.243.233', '18.204.20.81']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ This is the function for deploying the content """
    try:
        file_name = archive_path.split("/")[-1]
        p = "/data/web_static/releases/" + file_name.strip(".tgz")
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp")
        run("mkdir -p " + p)
        run("tar -xzf /tmp/" + file_name + " -C " + p)
        run("rm /tmp/" + file_name)
        run("mv " + p + "/web_static/* " + p)    
        run("rm -rf " + p + "/web_static")
        run("rm -rf " + sym_link)
        run("ln -s " + p + "/ " + sym_link)
        print("New version deployed!")
        return True
    except Exception:
        return False
