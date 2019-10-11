import datetime
import unittest
from unittest.mock import MagicMock

from hamb.handlers.email_handler import Handler, render_html, json_serial


class TestEmailHandler(unittest.TestCase):
    def test_email(self):
        print("----------------test_email")
        result = {"summary": {"status": "test", "manifest": "test"}}
        conf = {
            "hambot": {"environment": "dev"},
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
        html = render_html("hello")
        self.assertEqual(
            html,
            '<table border="1" cellpadding="0" cellspacing="0" bordercolor=#BLACK><tr> \
            <td> Jobs  Status </td> </tr><tr> <td>hello</td> \
            </tr></table> <br> <br><i>]</i>',
        )

    def test_serial_json(self):
        now = datetime.datetime.now()
        result = json_serial(now)
        self.assertEqual(result, now.isoformat())
