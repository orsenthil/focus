#!/usr/bin/env python3
"""
Focus

Time based focus work work. Widely known as the Pomodoro Technique.

1. How many work units?
2. Time for focussed work unit? 20 minutes
3. Time for disciplined break? 5 minutes
"""

import sys
import time
import subprocess

FOCUS_TIME = 20
DISCIPLINED_BREAK_TIME = 5


def work(work_units):
    """Work"""
    print("Starting focus time for {} work units".format(work_units))
    for work_unit in range(1, work_units + 1):
        print(f"Starting work unit {work_unit}")
        for t in range(1, FOCUS_TIME + 1):
            print(f"Focussing for {t} minutes.")
            time.sleep(60)
        print("disciplined break")
        subprocess.call(["open", "5-minute-music.mp3"])
        for t in range(1, DISCIPLINED_BREAK_TIME + 1):
            print(f"Break time for {t} minutes.")
            time.sleep(60)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: focus.py <work_units>")
        work_units = 2
    else:
        work_units = int(sys.argv[1])
    work(work_units)
