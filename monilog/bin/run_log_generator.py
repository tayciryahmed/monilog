import argparse
import logging
from monilog import LogGenerator


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rates", nargs='+', type=int, default=[11, 9])
    parser.add_argument("--durations", nargs='+',
                        type=int, default=[3*60, 3*60])
    args = parser.parse_args()

    if len(args.rates) != len(args.durations):
        raise ValueError(
            'You should have the same number of params rates and durations.'
        )

    for rate, duration in zip(args.rates, args.durations):
        logging.info(
            'Starting a new simulation setup with rate %d req/s and duration %d secs.\n'
            % (rate, duration)
        )
        LogGenerator(rate=rate).run(duration=duration)
