import sys

import argparse
from random import randint
from time import sleep
from colorama import Fore
from datetime import datetime

parser = argparse.ArgumentParser(description='Matrix Chain Multiplication Algorithm Test Script.')
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-c', '--numberofcases', type=int, help='Param = number of test cases to be generated...', required=True)
parser.add_argument('-t', '--time', help='Show run-time(s) in milliseconds for each test case.')

args = parser.parse_args()


def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxint
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n - 1]


case = args.c
runtime = args.time


def generate_test(case, runtime):
    print "Generating", case, " different test cases..."
    for i in range(0, case):
        call_param1 = []
        call_param2 = randint(2, 20)
        print (Fore.WHITE + "\nGenerating test : #" + str(i + 1))
        for k in range(0, call_param2):
            sleep(0.021)
            call_param1.append(randint(1, 100))
        print "\nGenerated Matrices : "
        print (Fore.WHITE + "-------------------------------")
        for z in range(0, call_param2 - 1):
            print (Fore.LIGHTBLUE_EX + str(call_param1[z]) + "x" + str(call_param1[z + 1])),
        print ""
        print (Fore.WHITE + "-------------------------------")
        arr = call_param1
        size = len(arr)
        print(Fore.LIGHTRED_EX + "Minimum number of multiplications is "),
        if runtime is not None:
            a = datetime.now()
            print str(MatrixChainOrder(arr, size))
            b = datetime.now()
            c = b - a
            print "Took : " + str(int(c.total_seconds() * 1000)) + "ms"
        else:
            print str(MatrixChainOrder(arr, size))
        sleep(0.8)


generate_test(case=case, runtime=runtime)