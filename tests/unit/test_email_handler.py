import datetime
import re
import unittest
from unittest.mock import MagicMock

from hamb.handlers.email_handler import Handler, render_html, json_serial


class TestEmailHandler(unittest.TestCase):
    def test_email(self):
        print("----------------test_email")
        result = {"summary": {"status": "test", "manifest": "test"}}
        conf = {
            "hamb": {"environment": "dev"},
            "aws": {
                "aws_key": "aws_key",
                "aws_id": "aws_id",
                "ses_def_sender": "ses_def_sender",
                "ses_region": "ses_region",
            },
        }
        test_class = Handler(CONF=conf)
        test_class.os = MagicMock()
        test_class.run(result, "email@equinox.com")
        self.assertEqual(True, conf is not None)

    def test_render_html(self):
        result = "hello"
        html = render_html(result)
        match = re.search(f"<td> {result} </td>", html)
        self.assertEqual(match.group(), f"<td> {result} </td>")

    def test_serial_json(self):
        now = datetime.datetime.now()
        result = json_serial(now)
        self.assertEqual(result, now.isoformat())
