try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'tester',
    'author': 'Leigh Michael Forrest',
    'url': 'http://github.com/lforrest/tester',
    'download_url': 'http://github.com/lforrest/tester.git',
    'author_emal': 'leigh@example.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tester'],
    'scripts': [],
    'name': 'tester'
}

setup(**config)
