import unittest

from unittest.mock import MagicMock
from hamb.sql_compare_list import SqlCompare


class TestSqlCompareList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_conf = dict()
        test_conf["label"] = "this is a test"
        test_conf["conn_a"] = "sample_connection_foo"
        test_conf["conn_b"] = "sample_connection_bar"
        test_conf["script_a"] = "select count(*) from sample"
        test_conf["script_b"] = "select count(*) from sample"
        test_conf["pct_diff"] = True
        test_conf["heartbeat"] = True
        cls.testClass = SqlCompare(test_conf)

    def test_success_run(self):
        self.testClass.conn_a = MagicMock()
        self.testClass.conn_b = MagicMock()

        self.testClass.run()
