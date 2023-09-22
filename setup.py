from setuptools import (setup, find_packages)
from vitass import (__VERSION__, __AUTHOR__, __AUTHOR_EMAIL__)

def get_requirements():
    return open('requirements.txt').read().splitlines()


setup(
    name="vitass",
    version=__VERSION__,
    packages=find_packages(),
    description='Digital vitenskapelig assistent',
    keywords=['designit', 'vitass', 'django', 'python'],
    license='GNUGPL-v3',
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    install_requires=get_requirements(),
)

