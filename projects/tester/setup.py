try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tester',
    'author': 'Leigh Forrest',
    'url': 'http://github.com/example/tester',
    'download_url': 'http://github.com/example/tester.git',
    'author_email': 'leigh@example.com',
    'version': '0.1',
    'install_requires': ['nose', 'wikipedia'],
    'packages': ['tester'],
    'scripts': ['math.py'],
    'name': 'math.py'
}

setup(**config)
