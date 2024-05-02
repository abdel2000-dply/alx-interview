#!/usr/bin/python3
import sys
import signal


def signal_handler(sig, frame):
    '''Signal handler for SIGINT'''
    print_stats()
    sys.exit(0)


def print_stats():
    '''Prints the stats of the log parsing'''
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {"200": 0, "301": 0, "400": 0, \
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            data = line.split()
            size = int(data[-1])
            status_code = data[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += size
        except e:
            pass
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
print_stats()
