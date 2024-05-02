#!/usr/bin/python3
''' stats module '''
import sys
import signal
import re
# Write a script that reads stdin line by line and computes metrics:

# Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> 
# (if the format is not this one, the line must be skipped)
# After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
# Total file size: File size: <total size>
# where <total size> is the sum of all previous <file size> (see input format above)
# Number of lines by status code:
# possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
# if a status code doesn’t appear or is not an integer, don’t print anything for this status code
# format: <status code>: <number>
# status codes should be printed in ascending order
# Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.
def signal_handler(signal, frame):
  ''' signal_handler function '''
  pass

def print_stats():
    ''' print_stats function '''
    print('File size: {}'.format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))

def parse_line(line):
  ''' parse_line function '''
  


def main():
  ''' main function '''
    


if __name__ == '__main__':
  status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
  total_size = 0
  line_count = 0
  signal.signal(signal.SIGINT, signal_handler)
  main()
