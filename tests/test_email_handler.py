import unittest

from hambot.handlers.email_handler import Handler
from cocore.config import Config



class TestEmailHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testClass = Handler()

    def test_email(self):
        print('----------------test_email')
        result = {'summary': {
            'status': 'test',
            'manifest': 'test'
        }}
        conf = Config()
        self.testClass.run(result, 'email@equinox.com')
        self.assertEqual(True, conf is not None)
