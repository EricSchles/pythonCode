try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Exercise 47 in LPTHW',
    'author': 'Eric Schles',
    'url':'N/A',
    'download_url':'N/A',
    'author_email':'N/A',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['ex47'],
    'scripts':[],
    'name':'ex47'
}

setup(**config)

