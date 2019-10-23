import unittest
from unittest.mock import MagicMock

from hamb.handlers.slack_handler import Handler


class TestSlackHandler(unittest.TestCase):
    def test_slack(self):
        print("----------------test_email")
        result = {"summary": {"status": "test", "manifest": "test"}}
        conf = {
            "hamb": {"environment": "dev"},
            "slack": {"token": "token", "bot_id": "bot_id"},
        }
        test_class = Handler(CONF=conf)
        test_class.sc = MagicMock()
        test_class.run(result, "test slack")
        self.assertEqual(True, conf is not None)
