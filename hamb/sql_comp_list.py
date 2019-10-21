"""
this will be the main entry point to the program
"""

from cocore.Logger import Logger
from codb.rdb_tools import DBInteraction

LOG = Logger()


class SqlComp(object):
    """

    """

    def __init__(self, test_conf):
        """

        :param test_conf:
        :return:
        """
        print(f"=====>>>>> test_conf: {test_conf}")
        self.test_conf = test_conf
        self.conn_a = self.test_conf["conn_a"]
        self.conn_b = self.test_conf["conn_b"]
        print(f"conn_a: {self.conn_a}")
        print(f"conn_b: {self.conn_b}")
        self.aws_access_key = None
        self.aws_secret_key = None

    def setup(self, CONF):
        print("Setting up...")

        self.aws_access_key = CONF["general"]["aws_access_key"]
        self.aws_secret_key = CONF["general"]["aws_secret_key"]

        self.conn_a = DBInteraction(self.conn_a)
        self.conn_b = DBInteraction(self.conn_b)

        return self

    def get_script(self, script):
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
                "aws_access_key": self.aws_access_key,
                "aws_secret_key": self.aws_secret_key,
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

        script_a = self.get_script(self.test_conf["script_a"])
        script_b = self.get_script(self.test_conf["script_b"])
        # warning_threshold = self.test_conf.get("warning_threshold", 1)
        # failure_threshold = self.test_conf.get("failure_threshold", 1)
        # percent_diff = self.test_conf.get("pct_diff", False)
        # heartbeat = self.test_conf.get("heartbeat", False)

        LOG.l(
            "\n----------------------\
            -------------------------\
            ----------------------\n"
            + label
            + "\n--------------------\
            -------------------------\
            ------------------------\n"
        )

        LOG.l("\nscript_a: \n" + script_a + "\n")
        LOG.l("script_b: \n" + script_b + "\n")

        res_a = self.conn_a.fetch_sql_all(script_a).fetchall()
        result_a = [i[0] for i in res_a]
        res_b = self.conn_b.fetch_sql_all(script_b).fetchall()
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
