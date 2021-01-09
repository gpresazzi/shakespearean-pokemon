import poke_restapi.main as main
from unittest.mock import Mock, ANY

def test_run(mocker):
    mock_unicorn_run = mocker.patch("poke_restapi.main.uvicorn.run", return_value=Mock())
    
    main.run()
    mock_unicorn_run.assert_called_with(ANY, host="0.0.0.0", port=8000)