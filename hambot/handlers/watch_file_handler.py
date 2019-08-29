"""
drops watch file in ftp folder per [hambot] config section
"""
from time import time, sleep
import ftplib
from cocore.Logger import Logger
from cocore.config import Config

CONF = Config()
LOG = Logger()


class Handler(object):
    def __init__(self):
        pass

    @staticmethod
    def run(result, conf):
        environment = CONF['hambot']['environment']
        ftp_site = CONF['hambot_ftp']['site']
        ftp_user = CONF['hambot_ftp']['user']
        ftp_password = CONF['hambot_ftp']['password']
        ftp_path = CONF['hambot_ftp']['path']

        level = result['summary']['status']

        # we are hardcoded to never write a success file on failure --> probably a good idea?
        if level == 'failure':
            LOG.l('exiting')
            return

        file_name = str(environment).lower() + '_' + conf

        ftp = ftplib.FTP(ftp_site)
        ftp.login(ftp_user, ftp_password)
        path = ftp_path
        ftp.cwd(path)

        LOG.l('listing files:')
        for f in ftp.nlst():
            LOG.l(f)
            if f == file_name:
                ftp.delete(f)

        with open(file_name, 'wb') as f:
            f.write('yippee')

        sleep(10)

        LOG.l("uploading to FTP")
        ftp.storbinary('STOR ' + file_name, open(file_name, 'rb'))
        LOG.l("FTP upload complete")

        ftp.quit()
