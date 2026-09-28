import json
from unittest.mock import MagicMock

from app import Handler


def test_root_response():
    handler = Handler.__new__(Handler)
    handler.path = "/"

    handler.send_response = MagicMock()
    handler.send_header = MagicMock()
    handler.end_headers = MagicMock()
    handler.wfile = MagicMock()

    Handler.do_GET(handler)

    handler.send_response.assert_called_once_with(200)

    args = handler.wfile.write.call_args[0]
    body = json.loads(args[0].decode())

    assert body["status"] == "ok"
    assert body["service"] == "python-devops-demo"
