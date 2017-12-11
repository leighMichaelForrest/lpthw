try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'lexicon',
    'author': 'Leigh Forrest',
    'url': '',
    'download_url': '',
    'author_email': 'leighmforrest@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'lexicon'
}

setup(**config)
