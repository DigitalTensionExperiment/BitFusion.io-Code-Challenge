from setuptools import setup

setup(
    name='',
    version='1.0',
    py_modules=['restfulFlaskAPI'],
    install_requires=[
        'Click',
        'Docker',
    ],
    entry_points='''
        [console_scripts]
        restfulFlaskAPI=restfulFlaskAPI:cli
    ''', 
)