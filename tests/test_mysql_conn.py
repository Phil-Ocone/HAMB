import unittest

from cocore.config import Config
from hambot.handlers.sql_comp import Test
from unittest.mock import patch

class TestTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        conf = Config()

        test_conf = dict()
        test_conf['label'] = 'this is a mysql test'
        test_conf['conn_a'] = 'sample_mysql_connection'
        test_conf['conn_b'] = 'sample_mysql_connection'
        test_conf['script_a'] = 'select 0'
        test_conf['script_b'] = 'select 0'
        test_conf['pct_diff'] = True
        test_conf['heartbeat'] = True
        self.testClass = Test(test_conf)

    def test_run(self):
      with patch('codb.rdb_tools.DBInteraction.fetch_sql_one', return_value = [{}]):
        self.testClass.run()
