import unittest

from unittest.mock import MagicMock
from hamb.sql_comp import SqlComp


class TestSqlComp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_success_run(self):
        test_conf = dict()
        test_conf["label"] = "this is a test success"
        test_conf["conn_a"] = "sample_connection_foo"
        test_conf["conn_b"] = "sample_connection_bar"
        test_conf["script_a"] = "select count(*) from sample"
        test_conf["script_b"] = "select count(*) from sample"
        test_conf["pct_diff"] = True
        test_conf["heartbeat"] = True
        self.testClass = SqlComp(test_conf)

        self.testClass.conn_a = MagicMock()
        self.testClass.conn_b = MagicMock()

        self.testClass.run()
