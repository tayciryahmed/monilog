import os
from datetime import datetime
from collections import Counter
from monilog import LogGenerator

tmp_file = '/tmp/test'


def test_generate_log():
    log_values = LogGenerator().generate_log(
        datetime.now()).split()
    assert len(log_values) == 10
    assert log_values[5].strip(
        "\"") in ["GET", "POST", "POST", "PUT", "DELETE"]
    assert log_values[8][0] < '6'


def test_random_ip():
    rand_ip = LogGenerator().random_ip()
    assert Counter(rand_ip)['.'] == 3
    for x in rand_ip.split('.'):
        assert int(x) < 256


def test_write_log():
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    LogGenerator(
        file=tmp_file
    ).write_log(
        datetime.now()
    )

    assert len(open(tmp_file, 'r').readline()) > 1


def test_run():
    LogGenerator(file=tmp_file).run(duration=1)
    assert len(open(tmp_file, 'r').readline()) > 1
