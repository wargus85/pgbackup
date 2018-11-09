pgbackup
========

CLI for backing up remote PostgreSQL database either locally or to S3

Preparing the Development Environment
-------------------------------------

1. Ensure that ``pip`` and ``pipenv`` are installed.
2. Clone the repository ``git clone git@github.com/wargus85/pgbackup``
3. ``cd`` into the repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv ``python3 -m pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination.

SE Example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

   $ pgbackup postgres://bob@example.com:5432/db_one --driver local /path/to/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is Activate

::

    $make

If virtualenv isn't active then use:

::

    $ python3 -m pipenv run make