from monilog import Parser


def test_parser():
    parser = Parser()
    log_line = """127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123"""
    parsed_log = parser(log_line)
    assert len(parsed_log) == 7
    assert isinstance(parsed_log, dict)
