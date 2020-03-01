# manage the pipeline : reading the logs, sending them to the stats then send
# stats to alerting and display both

import time
import logging  
import argparse

log_format='%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)

HIGH_TRAFFIC_DUR = 2*60
STAT_DUR = 10

class MonilogPipeline:
    def __init__(self, 
                 file='/tmp/access.log', 
                 threshold=10):
        self.file = file 
        self.threshold = threshold
    
    def parse_log(self, line):
        return {'time': '1s' ,
                'type': 'http'}
    
    def generate_stats(self, traffic_buffer):
        logging.info('10 s ')
    
    def run(self):
        alert = False
        high_traffic_nb = 0
        traffic_buffer = []

        file = open(self.file)

        stat_time = time.time()
        high_traffic_time = time.time()

        while True:
            line = file.readline()
            if not line:
                continue
            else:
                traffic_buffer.append(
                    self.parse_log(line)
                )
                high_traffic_nb += 1


                if time.time() - stat_time >= STAT_DUR:
                    self.generate_stats(traffic_buffer)
                    stat_time = time.time()
                    traffic_buffer = []
                
                if time.time() - high_traffic_time >= HIGH_TRAFFIC_DUR:
                    if high_traffic_nb/HIGH_TRAFFIC_DUR > self.threshold and not alert:

                        alert = True

                        logging.warning(
                            "High traffic generated an alert - hits = %f, triggered at %s"
                            % (
                                high_traffic_nb/HIGH_TRAFFIC_DUR,
                                time.strftime('%d/%b/%Y:%H:%M:%S')

                            )
                            )

                    elif high_traffic_nb/HIGH_TRAFFIC_DUR <= self.threshold and alert : 
                        logging.info(
                            "The high traffic alert is recovered at %s"
                            % (time.strftime('%d/%b/%Y:%H:%M:%S'))
                            )

                    high_traffic_time = time.time()
                    high_traffic_nb = 0


        
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/tmp/access.log")
    parser.add_argument("--threshold", default=10)
    args = parser.parse_args()

    monilog_pipeline = MonilogPipeline(
        file=args.file,
        threshold=args.threshold
    )

    monilog_pipeline.run()
    




