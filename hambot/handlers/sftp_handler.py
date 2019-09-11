"""
drops watch file in sftp folder per [hambot] config section
"""
from time import time, sleep
from cocore.Logger import Logger
from cocore.config import Config
from coutils.ftp_tools import FTPInteraction

LOG = Logger()


class Handler(object):
    def __init__(self, CONF):
        self.host = CONF["hambot_sftp"]["site"]
        self.user = CONF["hambot_sftp"]["user"]
        self.password = CONF["hambot_sftp"]["password"]
        self.environment = CONF["hambot"]["environment"]
        self.path = CONF["hambot_sftp"]["path"]
        self.SFTP = None

    def setup(self):
        self.SFTP = FTPInteraction(
            protocol="sftp", host=self.host, user=self.user, password=self.password
        )

        return self

    def run(self, result, conf):
        level = result["summary"]["status"]

        # we are hardcoded to never write a success file on failure --> probably a good idea?
        if level == "failure":
            LOG.l("exiting")
            return

        file_name = str(self.environment).lower() + "_" + conf

        self.SFTP.conn()
        self.SFTP.sftp_conn.chdir(self.path)

        LOG.l("listing files:")
        for f in self.SFTP.sftp_conn.listdir():
            LOG.l(f)
            if f == file_name:
                self.SFTP.sftp_conn.remove(f)

        with open(file_name, "wb") as f:
            f.write("yippee")

        sleep(10)

        LOG.l("uploading to SFTP")
        self.SFTP.write_file(file_name, self.path)
        LOG.l("SFTP upload complete")

        self.SFTP.quit()
