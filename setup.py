from setuptools import setup, find_packages

with open('README.rst',encoding='UTF-8') as r:
    readme = r.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description = readme,
    author = 'Warren',
    author_email = 'warren.argus@curtin.edu.au',
    install_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'':'src'}, #this is a legacy thing that we do because of the above line
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)