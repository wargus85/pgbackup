import pytest

from pgbackup import cli

url = 'postgres://bob@example.com:5432/db_one'

@pytest.fixture
def parser():
        return cli.create_parser()

def test_parser_without_driver(parser):
    '''
    Without a specified driver the parser will exit
    '''
    with pytest.raises(SystemExit):
       # parser = cli.create_parser() # this line can be commented out from all the tests once we add the pytest.fixture in
        parser.parse_args([url])      # we then need to pass in the pytest fixture to the test definition
    
def test_parser_with_driver():
    '''
    The parser will exit if it receives a driver without a destination
    '''
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url,"--driver","local"])

def test_parser_with_unknown_driver():
        '''
        The parser will exit if the driver name is unknown'
        '''
        parser = cli.create_parser()

        with pytest.raises(SystemExit):
                parser.parse_args([url,'--driver','azure','destination'])

def test_parser_with_known_drivers():
        '''
        The parser will not exit if the driver name is known
        '''
        parser = cli.create_parser()

        for driver in ['local','s3']:
            assert parser.parse_args([url,'--driver',driver,'destination'])
   

def test_parser_with_driver_and_destination():
    """
    The parser will not exist if it receives a driver and destination
    """
    parser = cli.create_parser()

    args = parser.parse_args([url, '--driver', 'local','/some/path'])    

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'

