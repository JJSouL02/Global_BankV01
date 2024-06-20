from setuptools import setup, find_packages

setup(
    name='bank_app',
    version='0.1',
    packages=find_packages(),
    scripts=['bank_v02.py', 'Cuenta.py', 'tictactoe.py'],

    # Metadata
    author='Jesus Jiménez Simón',
    author_email='jesus@example.com',
    description='A simple banking application with tic-tac-toe game integration.',
    license='MIT',
    keywords='banking tictactoe game',

    # Dependencies
    install_requires=[
        'getpass',  # Example because dont need install requeriments
    ],

    # Entry points
    entry_points={
        'console_scripts': [
            'bank_app = bank_v02:main',
        ],
    },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)