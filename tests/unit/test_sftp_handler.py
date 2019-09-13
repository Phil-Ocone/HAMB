import unittest
from unittest.mock import MagicMock

from hambot.handlers.sftp_handler import Handler


class TestSFTPHandler(unittest.TestCase):

    def test_sftp(self):
        print('----------------test_email')
        result = {'summary': {
            'status': 'test',
            'manifest': 'test'
        }}
        conf = {
            "hambot": {
                "environment": "dev"
            },
            "hambot_sftp": {
                "site": "site",
                "user": "user",
                "password": "password",
                "path": "path"
            }
        }

        test_class = Handler(CONF=conf)
        test_class.SFTP = MagicMock()
        test_class.run(result, 'any text')
        self.assertEqual(True, conf is not None)
