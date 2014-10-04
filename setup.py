from setuptools import setup, find_packages


SCRIPTS = [
    'z = z.scripts.single:main',
    'zall = z.scripts.extra:main',
    'zload = z.scripts.extra:l',
    'zdump = z.scripts.extra:d',
]

setup(
    name = 'z',
    version = '0.1',
    entry_points = {'console_scripts': SCRIPTS },
    packages = find_packages(),
    install_requires = ['argh']
)
