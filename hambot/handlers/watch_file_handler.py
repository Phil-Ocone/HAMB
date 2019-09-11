"""
drops watch file in ftp folder per [hambot] config section
"""
from time import time, sleep
import ftplib
from cocore.Logger import Logger

LOG = Logger()


class Handler(object):
    def __init__(self, CONF):
        self.environment = CONF["hambot"]["environment"]
        self.site = CONF["hambot_ftp"]["site"]
        self.user = CONF["hambot_ftp"]["user"]
        self.password = CONF["hambot_ftp"]["password"]
        self.path = CONF["hambot_ftp"]["path"]

        self.ftp = None

    def setup(self):
        self.ftp = ftplib.FTP(self.ftp_site)
        self.ftp.login(self.ftp_user, self.ftp_password)

        return self

    def run(self, result, conf):
        level = result["summary"]["status"]

        # we are hardcoded to never write a success file on failure --> probably a good idea?
        if level == "failure":
            LOG.l("exiting")
            return

        file_name = str(self.environment).lower() + "_" + conf

        path = self.ftp_path
        self.ftp.cwd(path)

        LOG.l("listing files:")
        for f in self.ftp.nlst():
            LOG.l(f)
            if f == file_name:
                self.ftp.delete(f)

        with open(file_name, "wb") as f:
            f.write("yippee")

        sleep(10)

        LOG.l("uploading to FTP")
        self.ftp.storbinary("STOR " + file_name, open(file_name, "rb"))
        LOG.l("FTP upload complete")

        self.ftp.quit()
