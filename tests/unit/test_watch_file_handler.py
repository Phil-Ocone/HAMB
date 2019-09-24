import unittest
from unittest.mock import MagicMock

from hambot.handlers.watch_file_handler import Handler


class TestWatchFileHandler(unittest.TestCase):
    def test_watch_file_handler(self):
        print("----------------test_watch_file_handler")
        result = {"summary": {"status": "test", "manifest": "test"}}
        conf = {
            "hambot": {"environment": "dev"},
            "hambot_ftp": {
                "site": "site",
                "user": "user",
                "password": "password",
                "path": "path",
            },
        }

        test_class = Handler(CONF=conf)
        test_class.ftp = MagicMock()
        test_class.run(result, "email@equinox.com")
        self.assertEqual(True, conf is not None)

    def test_watch_file_handler_failure(self):
        print("----------------test_watch_file_handler_failure")
        result = {"summary": {"status": "failure", "manifest": "test"}}
        conf = {
            "hambot": {"environment": "dev"},
            "hambot_ftp": {
                "site": "site",
                "user": "user",
                "password": "password",
                "path": "path",
            },
        }

        test_class = Handler(CONF=conf)
        test_class.ftp = MagicMock()
        test_class.run(result, "email@equinox.com")
        self.assertEqual(True, conf is not None)
