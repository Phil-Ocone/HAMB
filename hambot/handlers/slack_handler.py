"""
here is where the slack handler will go
"""
from cocore.config import Config
from slackclient import SlackClient

CONF = Config()


class Handler(object):
    @staticmethod
    def run(result, conf):

        slack_token = CONF['slack']['token']
        slack_channel = conf
        bot_id = str(CONF['slack']['bot_id'])
        sc = SlackClient(slack_token)
        # print sc.api_call("api.test")
        # print sc.api_call("channels.info", channel="C2JPQAHEW")
        # print "this is slack handler"
        print(sc.api_call(
            "chat.postMessage", channel=slack_channel, username='hambot', as_user="true",
            text=result['summary'],
        ))
        # print result['summary']['status']
        # print result['detail']
        # print result.get('summary')

    # slack_message()
