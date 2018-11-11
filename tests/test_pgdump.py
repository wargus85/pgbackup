import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
    '''
    Utilise pg_dump wih the database URL
    '''
    mocker.patch('subprocess.Popen')
    assert pgdump(url)
    subprocess.Popen.assert_called_with(['pg_dump',url], stdout=subprocess.PIPE)