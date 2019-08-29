"""
drops watch file in sftp folder per [hambot] config section
"""
from time import time, sleep
from cocore.Logger import Logger
from cocore.config import Config
from coutils.ftp_tools import FTPInteraction

CONF = Config()
LOG = Logger()

SFTP = FTPInteraction(protocol='sftp', host=CONF['hambot_sftp']['site'],
                     user=CONF['hambot_sftp']['user'],
                     password=CONF['hambot_sftp']['password'])


class Handler(object):
    def __init__(self):
        pass

    @staticmethod
    def run(result, conf):
        environment = CONF['hambot']['environment']
        sftp_path = CONF['hambot_sftp']['path']

        level = result['summary']['status']

        # we are hardcoded to never write a success file on failure --> probably a good idea?
        if level == 'failure':
            LOG.l('exiting')
            return

        file_name = str(environment).lower() + '_' + conf

        SFTP.conn()
        path = sftp_path
        SFTP.sftp_conn.chdir(path)

        LOG.l('listing files:')
        for f in SFTP.sftp_conn.listdir():
            LOG.l(f)
            if f == file_name:
                SFTP.sftp_conn.remove(f)

        with open(file_name, 'wb') as f:
            f.write('yippee')

        sleep(10)

        LOG.l("uploading to SFTP")
        SFTP.write_file(file_name, path)
        LOG.l("SFTP upload complete")

        SFTP.quit()
