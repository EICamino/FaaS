#!/usr/bin/env python3

import time
import functions

# ===== config =====

# tests to run
tests = {
    # testName: (testFunction, arguments)
    "Fibonacci": (functions.fib, 30)
}

# number of times to run
num = 10

if __name__ == "__main__":
    for pair in tests:
        testName, (testF, *args) = pair, tests[pair]

        print("===== running %s test =====" % testName)
        # print("Parameters:", *args)
        functions.timer(num, testF, *args)
