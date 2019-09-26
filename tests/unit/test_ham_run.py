import unittest
import datetime
from unittest.mock import patch

from hambot.ham_run_utility import json_serial, TestEngine, HandlerEngine


class TestHamrun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run(self):
        test_config = {'sample_sql_comp_test': {}}
        test_config['sample_sql_comp_test']['label'] = 'this is a test'
        test_config['sample_sql_comp_test']["type"] = "sample_test_handler"
        test_config['sample_sql_comp_test']['conn_a'] = 'sample_connection_foo'
        test_config['sample_sql_comp_test']['conn_b'] = 'sample_connection_bar'
        test_config['sample_sql_comp_test']['script_a'] = 'select count(*) from sample'
        test_config['sample_sql_comp_test']['script_b'] = 'select count(*) from sample'
        test_config['sample_sql_comp_test']['pct_diff'] = True
        test_config['sample_sql_comp_test']['heartbeat'] = True
        with patch('hambot.ham_run_utility.TestEngine.manifest_reader', return_value=test_config),\
                patch('hambot.ham_run_utility.HandlerEngine.get_handler_config', return_value={}):
            result = self.TestEngine.run('sample')
            self.HandlerEngine.run('sample', result)

    def test_json_serial(self):
        json_serial(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
