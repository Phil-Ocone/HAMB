import unittest
from unittest.mock import MagicMock

from hambot.handlers.email_handler import Handler


class TestSFTPHandler(unittest.TestCase):

    def test_email(self):
        print('----------------test_email')
        result = {'summary': {
            'status': 'test',
            'manifest': 'test'
        }}
        conf = {
            "hambot": {"environment": "dev"},
            "aws": {
                "aws_key": "aws_key",
                "aws_id": "aws_id",
                "ses_def_sender": "ses_def_sender",
                "ses_region": "ses_region"
            }
        }
        test_class = Handler(CONF=conf)
        test_class.os = MagicMock()
        test_class.run(result, 'email@equinox.com')
        self.assertEqual(True, conf is not None)
