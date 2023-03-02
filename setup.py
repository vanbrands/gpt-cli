from setuptools import setup, find_packages

setup(
    name='gpt-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'rich',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'gpt-cli = main:main'
        ]
    }
)