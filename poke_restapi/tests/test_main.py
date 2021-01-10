import poke_restapi.main as main
from unittest.mock import Mock, ANY

def test_run(mocker):
    mocker.patch("poke_restapi.main.sys.argv", return_value=[])
    mock_unicorn_run = mocker.patch("poke_restapi.main.uvicorn.run", return_value=Mock())
    
    main.run()
    mock_unicorn_run.assert_called_with(ANY, host="0.0.0.0", port=8000)

def test_init_default(mocker):
    mocker.patch("sys.argv", ['cmd.py',])

    args = main.init()

    assert args.verbose == 0
    assert args.port == 8000
    assert args.disable_json == False

def test_init_verbose_and_port(mocker):
    mocker.patch("sys.argv", ['cmd.py', '--verbose', '--port', '8080'])
    
    args = main.init()
    
    assert args.verbose == 1
    assert args.port == 8080
    assert args.disable_json == False


def test_init_verbose_and_disable_json(mocker):
    mocker.patch("sys.argv", ['cmd.py', '--verbose', '--disable-json'])

    args = main.init()

    assert args.verbose == 1
    assert args.port == 8000
    assert args.disable_json == True
    