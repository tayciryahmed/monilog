import os
import re
import monilog
from monilog.utils import init_logger


def test_init_logger():
    _ = init_logger()
    root_path = '/'.join(
        monilog.__file__.split('/')[:-2]
    )
    found = False
    filename_re = 'simulation-(.*?).log'
    for filename in os.listdir(root_path):
        if re.search(filename_re, filename):
            found = True

    assert found
