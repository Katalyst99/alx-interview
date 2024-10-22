#!/usr/bin/python3
"""Then module for Log parsing"""
import sys
import re

sizeSum = 0
lCount = 0
sCodes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

log_format = (
    r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)'
)


def parse_logstats():
    """Reads stdin line by line and computes metrics"""

    print('File size: {}'.format(sizeSum))
    for code, val in sorted(sCodes.items()):
        if val > 0:
            print(f'{code}: {val}')


try:
    for line in sys.stdin:
        match = re.match(log_format, line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            sizeSum += file_size

            if status_code in sCodes.keys():
                sCodes[status_code] += 1

            lCount += 1
            if lCount % 10 == 0:
                parse_logstats()
except KeyboardInterrupt:
    parse_logstats()
    raise
