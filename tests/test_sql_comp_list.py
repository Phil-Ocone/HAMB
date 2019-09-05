import unittest

from unittest.mock import patch, MagicMock
from cocore.config import Config
from hambot.handlers.sql_comp_list import Test
from codb.rdb_tools import DBInteraction

class TestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conf = Config()

        test_conf = dict()
        test_conf['label'] = 'this is a test'
        test_conf['conn_a'] = 'sample_connection_foo'
        test_conf['conn_b'] = 'sample_connection_bar'
        test_conf['script_a'] = 'select count(*) from sample'
        test_conf['script_b'] = 'select count(*) from sample'
        test_conf['pct_diff'] = True
        test_conf['heartbeat'] = True
        cls.testClass = Test(test_conf)

    def test_success_run(self):
        db = DBInteraction
        db.fetchall = MagicMock(side_effect=['1','1'])
        with patch('codb.rdb_tools.DBInteraction.fetch_sql_all', return_value = db):
            status, details = self.testClass.run()
            self.assertEqual('success', status)

    def test_failed_run(self):
        db = DBInteraction
        db.fetchall = MagicMock(side_effect=['1','0'])
        with patch('codb.rdb_tools.DBInteraction.fetch_sql_all', return_value = db):
            status, details = self.testClass.run()
            self.assertEqual('failure', status)
