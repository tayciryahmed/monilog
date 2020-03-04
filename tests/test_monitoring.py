import os
import re
import monilog
from monilog import MonilogPipeline
from monilog import LogGenerator

tmp_file = '/tmp/test'


def test_run():
    if not os.path.exists(tmp_file):
        os.mknod(tmp_file)
    monitoring_pipeline = MonilogPipeline()
    monitoring_pipeline.stop_monitoring()
    monitoring_pipeline.run()

    root_path = '/'.join(
        monilog.__file__.split('/')[:-2]
    )
    found = False
    filename_re = 'simulation-(.*?).log'
    for filename in os.listdir(root_path):
        if re.search(filename_re, filename):
            found = True

    assert found
