import unittest
import datetime
from cocore.config import Config
from hambot.ham_run_utility import TestEngine, HandlerEngine, json_serial
from unittest.mock import patch

class TestHamrun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run(self):
        with patch('codb.rdb_tools.DBInteraction.fetch_sql_one', return_value = [{}]):
            result = self.TestEngine.run('sample')
            self.HandlerEngine.run('sample', result)

    def test_json_serial(self):
        json_serial(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
