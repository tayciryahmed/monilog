import os
import time
import random
import argparse
from time import sleep
from datetime import datetime
import logging

log_format = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)


class LogGenerator:
    def __init__(self,
                 file="/tmp/access.log",
                 rate=700):
        self.file = file
        self.rate = rate

        self.ips = ["::1", "192.168.0.110", "127.0.0.1", "60.242.26.14"]
        self.methods = ["GET", "GET", "GET", "POST", "POST", "PUT", "DELETE"]
        self.sections = ["/img", "/captcha", "/css", "/foo", "/foo", "/bar"]
        self.codes = ["200", "200", "200", "200", "200", "304", "403", "404", "501"]

    def write_log(self, timestamp):
        with open(self.file, 'a+', os.O_NONBLOCK) as f:
            f.write(self.generate_log(timestamp))
            f.flush()
            f.close()

    def random_ip(self):
        return str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) \
            + "." + str(random.randint(0, 255)) + "." \
            + str(random.randint(0, 255))

    def generate_log(self, timestamp):
        ip = random.choice([random.choice(self.ips), self.random_ip()])
        method = random.choice(self.methods)
        section = random.choice(self.sections) \
            + random.choice([".html", 
                             random.choice(self.sections)+'/',
                             random.choice(self.sections)+'/'])
        code = random.choice(self.codes)
        size = random.randint(10, 100000)
        return ('%s - - [%s +1000] "%s %s HTTP/1.1" %s %d\n'
                % (ip,
                   timestamp.strftime("%d/%b/%Y:%H:%M:%S"),
                   method,
                   section,
                   code,
                   size))

    def run(self, duration):
        start = time.time()
        while time.time()-start < duration:
            self.write_log(datetime.now())
            sleep(random.random()*2/self.rate)

