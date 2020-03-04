import argparse
from monilog import MonilogPipeline


def run():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="/tmp/access.log")
    parser.add_argument("--threshold", default=10, type=int)
    args = parser.parse_args()

    monilog_pipeline = MonilogPipeline(
        file=args.file,
        threshold=args.threshold
    )

    monilog_pipeline.run()

if __name__ == '__main__':
    run()