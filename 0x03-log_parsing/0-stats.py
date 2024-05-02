#!/usr/bin/python3
''' stats module '''
import sys
import signal
import re


def signal_handler(signal, frame):
    ''' signal_handler function '''
    print_stats()
    sys.exit(0)


def print_stats():
    ''' print_stats function '''
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))


def parse_line(line):
    ''' parse_line function '''
    global total_size, line_count, status_codes
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'  # nopep8
    try:
        match = re.fullmatch(pattern, line.strip())
        if match:
            status_code, size = match.groups()
            total_size += int(size)
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
    except Exception:
        pass


def main():
    ''' main function '''
    for line in sys.stdin:
        parse_line(line)
        if line_count % 10 == 0:
            print_stats()


if __name__ == '__main__':
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    line_count = 0
    signal.signal(signal.SIGINT, signal_handler)
    main()
