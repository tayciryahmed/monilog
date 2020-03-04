from datetime import datetime


class Parser:
    def __call__(self, log_line):
        parsed_log = {}
        log_values = log_line.split(' ')

        parsed_log['ip'] = log_values[0]
        parsed_log['time'] = datetime.strptime(
            log_values[3].strip("[]"),
            "%d/%b/%Y:%H:%M:%S")

        parsed_log['method'] = log_values[5].strip("\"")

        parsed_log['sections'] = log_values[6].split('/')
        if len(parsed_log['sections']) > 2:
            parsed_log['section'] = parsed_log['sections'][1]
        else:
            parsed_log['section'] = "root"

        parsed_log['code'] = log_values[8]

        if log_values[9].strip("\n") == "-":
            parsed_log['size'] = 0
        else:
            parsed_log['size'] = int(log_values[9].strip("\n"))

        return parsed_log
