"""
this will be the main entry point to the program, will probably end up being a flask web service, with a basic UI
"""

import sys, os

# from pprint import pprint
from cocore.Logger import Logger
from cocore.config import Config
from codb.rdb_tools import DBInteraction

CONF = Config()
LOG = Logger()


class Test(object):
    """

    """

    def __init__(self, test_conf):
        """

        :param test_conf:
        :return:
        """
        print(f"=====>>>>> test_conf: {test_conf}")
        self.test_conf = test_conf

    @staticmethod
    def get_script(script):
        """

        :param script:
        :return:
        """

        def expand_params(sql):
            """
            substitutes params in sql stagement
            :param sql:
            :param params:
            :return: sql, expanded with params
            """

            params = {
                "aws_access_key": CONF["general"]["aws_access_key"],
                "aws_secret_key": CONF["general"]["aws_secret_key"],
            }

            for p in params.keys():
                var = "$[?" + p + "]"
                val = str(params[p])
                sql = sql.replace(var, val)
            return sql

        if script[-4:] == ".sql":
            with open(script, "r") as myfile:
                script_data = myfile.read()
        else:
            script_data = script

        script_data = expand_params(script_data)
        return script_data

    def run(self):
        """

        :return:
        """
        label = self.test_conf["label"]
        conn_a = self.test_conf["conn_a"]
        conn_b = self.test_conf["conn_b"]
        script_a = self.get_script(self.test_conf["script_a"])
        script_b = self.get_script(self.test_conf["script_b"])
        warning_threshold = self.test_conf.get("warning_threshold", 1)
        failure_threshold = self.test_conf.get("failure_threshold", 1)
        percent_diff = self.test_conf.get("pct_diff", False)
        heartbeat = self.test_conf.get("heartbeat", False)

        LOG.l(
            "\n---------------------------------------------------------------------\n"
            + label
            + "\n---------------------------------------------------------------------\n"
        )
        print(f"conn_a: {conn_a}")
        print(f"conn_b: {conn_b}")

        conn_a = DBInteraction(conn_a)
        conn_b = DBInteraction(conn_b)

        LOG.l("\nscript_a: \n" + script_a + "\n")
        LOG.l("script_b: \n" + script_b + "\n")

        res_a = conn_a.fetch_sql_all(script_a).fetchall()
        result_a = [i[0] for i in res_a]
        res_b = conn_b.fetch_sql_all(script_b).fetchall()
        result_b = [i[0] for i in res_b]

        diff = list(set(result_a).symmetric_difference(set(result_b)))

        if diff:
            status = "failure"
        else:
            diff = None
            status = "success"

        detail = {
            "status": status,
            "test": label,
            "result_a": result_a,
            "result_b": result_b,
            "diff": diff,
            "test_conf": self.test_conf,
        }

        return status, detail
