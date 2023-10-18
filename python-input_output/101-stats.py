#!/usr/bin/python3
"""
Script reads stdin line by line and computes metrics

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
total file size and
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

format: File size: <total size>
format: <status code (in ascending order)>: <number>
"""


import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        elements = line.split()
        if len(elements) < 9:
            continue

        status_code = elements[-2]
        file_size = elements[-1]

        # Update total file size
        total_file_size += int(file_size)

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_code_counts.keys()):
                print("{}: {}".format(code, status_code_counts[code]))

except KeyboardInterrupt:
    pass

# Print the final statistics
print("File size: {}".format(total_file_size))
for code in sorted(status_code_counts.keys()):
    print("{}: {}".format(code, status_code_counts[code]))
