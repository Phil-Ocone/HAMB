import unittest

from cocore.config import Config
from hambot.handlers.sql_comp_list import Test

class TestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conf = Config()

        test_conf = dict()
        test_conf['label'] = 'this is a test'
        test_conf['conn_a'] = 'cosmo'
        test_conf['conn_b'] = 'cosmo'
        test_conf['script_a'] = 'select count(*) from edw_t.f_membership_contract'
        test_conf['script_b'] = 'select count(*) from edw_t.f_membership_contract'
        test_conf['pct_diff'] = True
        test_conf['heartbeat'] = True
        cls.testClass = Test(test_conf)

    def test_run(self):
        self.testClass.run()



