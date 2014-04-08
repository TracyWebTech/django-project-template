import os
import apt
import platform
import urllib

from apt import debfile
from distutils.version import StrictVersion


PUPPET_TARGET_VERSION="3.4.3-1puppetlabs1"
PUPPET_DIR = os.path.join(os.path.dirname(__file__))
MODULES_FILE = os.path.join(PUPPET_DIR, 'modules.txt')


def get_package(name):
    cache = apt.cache.Cache()
    if name in cache:
        return cache[name], cache

    return None, None


def pkg_available(name):
    pkg = get_package(name)[0]
    if pkg and pkg.versions.get(PUPPET_TARGET_VERSION):
        return True

    return False


def config_puppetlabs_repo():
    dist = platform.dist()[-1]

    url = 'http://apt.puppetlabs.com/puppetlabs-release-{}.deb'.format(dist)
    filename = '/tmp/puppet_apt.deb'
    try:
        urllib.urlretrieve(url, filename)
    except IOError:
        print "Could not install puppet"
        raise

    deb_pkg = debfile.DebPackage(filename)
    if deb_pkg.check():
        deb_pkg.install()
        cache = apt.cache.Cache()
        cache.update()
        cache.open()


def install_puppet(upgrade=False):
    pkg, cache = get_package('puppet')

    pkg.candidate = pkg.versions.get(PUPPET_TARGET_VERSION)
    if upgrade:
        pkg.mark_upgrade()
    else:
        pkg.mark_install()

    cache.commit()


# If the package not found or if the version is outdated, install puppet
if not pkg_available('puppet'):
    config_puppetlabs_repo()


pkg = get_package('puppet')[0]
if not pkg.is_installed:
    install_puppet()
elif apt.VersionCompare(pkg.installed.version, PUPPET_TARGET_VERSION) < 0:
    install_puppet(upgrade=True)
