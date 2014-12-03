#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

VERSION = (0, 1, 2)

if __name__ == '__main__':

    setup(
        name = 'vmguestlib',
        version = '0.1.2',
        author='Dag Wieers',
        author_email='dag@wieers.com',
        url='http://github.com/dagwieers/vmguestlib',
        download_url='http://github.com/dagwieers/vmguestlib/archive/0.1.2.tar.gz',
        description='Python API for interacting with VMware\'s VMGuestLib SDK',
        license = 'GPLv2',
        install_requires=['ctypes', ],
        py_modules = ['vmguestlib', ],
        scripts=[ 'vmguest-stats', ],
        keywords = ['Virtual', 'vmware', 'ESX', 'ESXi', 'VMGuestLib', 'SDK', 'API'],
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Software Development :: Testing',
            'Topic :: System :: Distributed Computing',
            'Topic :: System :: Emulators',
            'Topic :: System :: Hardware',
            'Topic :: System :: Operating System',
            'Topic :: System :: Systems Administration',
            'Topic :: Utilities'
        ],
        long_description='Python API for interacting with VMware\'s VMGuestLib SDK',
    )

# vim:ts=4:sw=4:et
