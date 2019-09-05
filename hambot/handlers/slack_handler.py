"""
here is where the slack handler will go
"""
from cocore.config import Config
from slackclient import SlackClient

CONF = Config()


class Handler(object):
    @staticmethod
    def run(result, conf):

        slack_token = CONF["slack"]["token"]
        slack_channel = conf
        bot_id = str(CONF["slack"]["bot_id"])
        sc = SlackClient(slack_token)
        print(
            sc.api_call(
                "chat.postMessage",
                channel=slack_channel,
                username="hambot",
                as_user="true",
                text=result["summary"],
            )
        )
