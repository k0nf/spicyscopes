from setuptools import setup

setup(
    name='spicyscopes',
    version='0.1.0',
    py_modules=['spicyscopes'],
    entry_points={
        'console_scripts': [
            'spicyscopes = spicyscopes:main'
        ]
    },
    install_requires=[
        'requests',
        'numpy',
        'pandas',
        'configparser',
        'argparse',
        'colorama'
    ],
)
