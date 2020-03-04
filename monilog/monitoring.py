# manage the pipeline : reading the logs, sending them to the stats then send
# stats to alerting and display both

import os
import sys
import time

from monilog.parser import Parser
from monilog.statistics import Statistics
from monilog.utils import init_logger

logger = init_logger()


HIGH_TRAFFIC_DUR = 2*60
STAT_DUR = 10
MAX_IDLE_TIME = 2*60


class MonilogPipeline:
    def __init__(self,
                 file='/tmp/access.log',
                 threshold=10):
        self.file = file
        self.threshold = threshold

    def run(self):
        parser = Parser()
        get_stats = Statistics(STAT_DUR)

        alert = False
        high_traffic_nb = 0
        traffic_buffer = []
        
        if not os.path.exists(self.file):
            time.sleep(1)

        file = open(self.file, 'r', os.O_NONBLOCK)

        stat_time = time.time()
        high_traffic_time = time.time()
        
        start_idle_time = None
        idle_duration = 0

        while True:
            line = file.readline()
            if not line:
                if not start_idle_time : 
                    start_idle_time = time.time()
                else:
                    idle_duration = time.time() - start_idle_time
                    if idle_duration > MAX_IDLE_TIME:
                        logger.info(
                            f'Monitoring stopped : Logging app not used for {int(idle_duration)}s.\n'
                        )
                        sys.exit(0)
                
            else:
                start_idle_time = None
                idle_duration = 0
                
                try:
                    parsed_line = parser(line)
                except:
                    logger.warning(f"There was an error parsing : {line}")
                    continue

                traffic_buffer.append(
                    parsed_line
                )
                high_traffic_nb += 1

                if time.time() - stat_time >= STAT_DUR:
                    logger.info('\n'+get_stats(traffic_buffer))
                    stat_time = time.time()
                    traffic_buffer = []

                if time.time() - high_traffic_time >= HIGH_TRAFFIC_DUR:
                    if high_traffic_nb/HIGH_TRAFFIC_DUR > self.threshold and not alert:

                        alert = True

                        logger.warning(
                            "High traffic generated an alert - hits = %f, triggered at %s.\n"
                            % (
                                high_traffic_nb/HIGH_TRAFFIC_DUR,
                                time.strftime('%d/%b/%Y %H:%M:%S')

                            )
                        )

                    elif high_traffic_nb/HIGH_TRAFFIC_DUR <= self.threshold and alert:
                        logger.info(
                            "The high traffic alert is recovered at %s.\n"
                            % (time.strftime('%d/%b/%Y %H:%M:%S'))
                        )

                    high_traffic_time = time.time()
                    high_traffic_nb = 0



