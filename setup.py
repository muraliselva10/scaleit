from setuptools import setup, find_packages

setup(
    name='auto_scaler',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'auto-scaler=auto_scaler.main:main',
        ],
    },
)
