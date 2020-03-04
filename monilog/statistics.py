from collections import Counter


class Statistics:
    def __init__(self, stat_dur):
        self.stat_dur = stat_dur

    def _get_mean_list(self, x):
        return sum(x)/len(x)

    def __call__(self, traffic_buffer):
        '''
        Args:
            traffic_buffer (list): Retrieved traffic logs.
            Each item of the list of the following structure:
                {
                    'ip': '127.0.0.1',
                    'time': '01/Mar/2020:16:50:04',
                    'method': 'GET',
                    'sections': ['api', 'user'],
                    'section': 'api',
                    'code': 304,
                    'size': 33256

                }
        Returns:
            stats (str): Statistics about the traffic.
        '''

        ans = 'The section of the website of the most hits is : '
        ans += Counter([x['section']
                        for x in traffic_buffer]).most_common(1)[0][0]
        ans += '.\nThe average number of hits per seconds is : '
        ans += str(len(traffic_buffer)/self.stat_dur)+'.\n'
        ans += 'The average size of requests is : '
        ans += str(self._get_mean_list([x['size'] for x in traffic_buffer]))
        ans += '.\nThe most frequent response code is : '
        ans += str(Counter([x['code']
                            for x in traffic_buffer]).most_common(1)[0][0])
        ans += '.\nThe most frequent method is : '
        ans += Counter([x['method']
                        for x in traffic_buffer]).most_common(1)[0][0]
        ans += '.\n'

        fq_4xx = len([
            x['code'] for x in traffic_buffer if x['code'][0] == '4']
        )/self.stat_dur
        if fq_4xx > 0:
            ans += f'The frequency of 4xx codes is : {fq_4xx} req per sec.\n'

        fq_5xx = len([
            x['code'] for x in traffic_buffer if x['code'][0] == '5']
        )/self.stat_dur
        if fq_5xx > 0:
            ans += f'The frequency of 5xx codes is : {fq_5xx} req per sec.\n'

        return ans
