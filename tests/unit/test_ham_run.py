import unittest
import datetime
from unittest.mock import patch

from hamb.ham_run_utility import json_serializer, TestEngine, HandlerEngine


class TestHamrun(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run_success(self):
        test_config = {"sample_sql_comp_test": {}}
        test_config["sample_sql_comp_test"]["label"] = "this is a test"
        test_config["sample_sql_comp_test"]["type"] = "sample_test_handler"
        test_config["sample_sql_comp_test"]["conn_a"] = "sample_connection_foo"
        test_config["sample_sql_comp_test"]["conn_b"] = "sample_connection_bar"
        test_config["sample_sql_comp_test"][
            "script_a"
        ] = "select count(*) from sample"
        test_config["sample_sql_comp_test"][
            "script_b"
        ] = "select count(*) from sample"
        test_config["sample_sql_comp_test"]["pct_diff"] = True
        test_config["sample_sql_comp_test"]["heartbeat"] = True
        with patch(
            "hamb.ham_run_utility.TestEngine.manifest_reader",
            return_value=test_config,
        ), patch(
            "hamb.ham_run_utility.HandlerEngine.get_handler_config",
            return_value={},
        ):
            result = self.TestEngine.run("sample")
            self.HandlerEngine.run("sample", result)

    def test_run_failure(self):
        test_config = {"sample_sql_comp_test": {}}
        test_config["sample_sql_comp_test"]["label"] = "this is a test"
        test_config["sample_sql_comp_test"][
            "type"
        ] = "sample_test_failed_handler"
        test_config["sample_sql_comp_test"]["conn_a"] = "sample_connection_foo"
        test_config["sample_sql_comp_test"]["conn_b"] = "sample_connection_bar"
        test_config["sample_sql_comp_test"][
            "script_a"
        ] = "select 1 from sample"
        test_config["sample_sql_comp_test"][
            "script_b"
        ] = "select 0 from sample"
        test_config["sample_sql_comp_test"]["pct_diff"] = True
        test_config["sample_sql_comp_test"]["heartbeat"] = True
        with patch(
            "hamb.ham_run_utility.TestEngine.manifest_reader",
            return_value=test_config,
        ), patch(
            "hamb.ham_run_utility.HandlerEngine.get_handler_config",
            return_value={},
        ):
            result = self.TestEngine.run("sample")
            self.HandlerEngine.run("sample", result)

    @staticmethod
    def test_json_serializer():
        json_serializer(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
