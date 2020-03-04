from monilog import Statistics


def test_get_mean_list():
    stats = Statistics(10)
    assert stats._get_mean_list([1, 2]) == 1.5


def test_statistics():
    stats = Statistics(10)
    assert isinstance(stats([{
        'ip': '127.0.0.1',
        'time': '01/Mar/2020:16:50:04',
        'method': 'GET',
        'sections': ['api', 'user'],
        'section': 'api',
        'code': '304',
        'size': 33256

    }]), str)
