import sys

import argparse
from random import randint
from time import sleep
from colorama import Fore
from datetime import datetime

parser = argparse.ArgumentParser(description='Matrix Chain Multiplication Algorithm Test Script.')
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-c', '--numberofcases', type=int, help='Param = number of test cases to be generated...',
                           required=True)
parser.add_argument('-t', '--time', help='Show run-time(s) in milliseconds for each test case.')
parser.add_argument('-r', '--recursive', help='Try to solve the problem by naive recursive algorithm.')
args = parser.parse_args()

caseParam = args.numberofcases
runTimeParam = args.time


def MatrixChainOrder(p, n):
    y=1
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
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
                    s[i][j] = k
    return m[1][n - 1], s
    # return {'res':m[1][n - 1], 'arr':s}


def print_optimal_parens(s, i, j):
    if i == j:
        print "A" + str(i),
    else:
        print "(",
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print ")",


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
            res, arr2 = MatrixChainOrder(arr, size)
            print str(res)
            b = datetime.now()
            print_optimal_parens(arr2, 1, size-1)
            c = b - a
            print "Took : " + str(long(c.total_seconds() * 10)) + "ms"
        else:
            res, arr2 = MatrixChainOrder(arr, size)
            print str(res)
            print_optimal_parens(arr2, 1, size-1)

        sleep(0.8)


generate_test(case=caseParam, runtime=runTimeParam)