#!/usr/bin/env python3
import time
import sys

# ===== Timer =====

def timer(n, function, *argv):

    timeStat = []

    for i in range(n):
        # start timing
        start = time.perf_counter()
        print("Running round %s ..." % (i + 1), end="\r")
        
        # exec function
        function(*argv)

        # stop timing
        timeStat.append(time.perf_counter() - start)
    
    # display time consuming for each round
    print("\nRun %s times, best: %4fs, worst: %4fs, avg: %4fs.\n" \
        % (n, max(timeStat), min(timeStat), sum(timeStat)/n))

# ===== Loading Test =====

# fibonacci function
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)