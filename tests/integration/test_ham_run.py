import unittest
import datetime
from hambot.ham_run_utility import TestEngine, HandlerEngine, json_serial


class TestHamrun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestEngine = TestEngine()
        cls.HandlerEngine = HandlerEngine()

    def test_run(self):
        result = self.TestEngine.run('sample')
        self.HandlerEngine.run('sample', result)

    def test_json_serial(self):
        json_serial(datetime.datetime(2015, 2, 1, 15, 16, 17, 345))
