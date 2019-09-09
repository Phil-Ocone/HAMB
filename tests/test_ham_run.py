import unittest
import datetime
from cocore.config import Config
from hambot.ham_run_utility import TestEngine, HandlerEngine, json_serial
from unittest.mock import patch, MagicMock
from codb.rdb_tools import DBInteraction

class TestHamrun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run(self):
        db = DBInteraction
        db.fetchall = MagicMock(side_effect=['1','1'])
        with patch('codb.rdb_tools.DBInteraction.fetch_sql_one', return_value = [{}]), patch('codb.rdb_tools.DBInteraction.fetch_sql_all', return_value = db):
                result = self.TestEngine.run('sample')
                self.HandlerEngine.run('sample', result)

    def test_json_serial(self):
        json_serial(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
