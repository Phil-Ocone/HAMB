import unittest
from unittest.mock import MagicMock

from hambot.handlers.slack_handler import Handler


class TestSlackHandler(unittest.TestCase):

    def test_email(self):
        print('----------------test_email')
        result = {'summary': {
            'status': 'test',
            'manifest': 'test'
        }}
        conf = {
            "hambot": {
                "environment": "dev"
            },
            "slack": {
                "token": "token",
                "bot_id": "bot_id"
            }
        }
        test_class = Handler(CONF=conf)
        test_class.sc = MagicMock()
        test_class.run(result, 'test slack')
        self.assertEqual(True, conf is not None)
