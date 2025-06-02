#!/usr/bin/python3
"""
This module provides a script that reads stdin and computes metrics.
Each 10 lines or after keyboard interruption, prints stats since beginning.
"""
import sys


def print_stats(total_size, status_counts):
    '''
    This function print the stats in stdout
    Args:
        total_size: Total size of the file
        status_count: Number of codes returned
    '''
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_count = {}
    valid_stat_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()

            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = parts[-1]

                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                if status_code in valid_stat_code:
                    status_count[status_code] = status_count.get(status_code, 0)+1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_count)

if __name__ == "__main__":
    main()
