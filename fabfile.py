from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration, use ssh-config for convensation.
env.use_ssh_config = True
production = 'vultr'
dest_path = '/sites/hr-note'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')


@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')

    cmd = ('rsync -ogavz --progress --delete'
           ' --exclude ".DS_Store" '
           'output/* vultr:/sites/hr-note/')
    local(cmd)


def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))


@hosts(production)
def nginx():
    """upload nginx config"""
    cmd = 'scp nginx_site.conf vultr:/tmp/nginx_site.conf'
    local(cmd)

    run('sudo mv /tmp/nginx_site.conf /etc/nginx/sites-available/hr-note')
    run('sudo chown root:root /etc/nginx/sites-available/hr-note')
    run('sudo ln -f -s /etc/nginx/sites-available/hr-note /etc/nginx/sites-enabled/hr-note')
    run('sudo nginx -s reload')


@hosts(production)
def clean_site():
    run("sudo rm -rf /sites/hr-note/*")
