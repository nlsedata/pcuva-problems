'''
Created on Jun 18, 2013

@author: Yubin Bai

All rights reserved.
'''

import time
from multiprocessing.pool import Pool
parallelSolve = False
INF = 1 << 30


def solve(par):
    r1 = '`1234567890-' + 'qwertyuiop[' + 'asdfghjhkl' + 'zxcvbnm,.'
    r2 = '1234567890-=' + 'wertyuiop[]' + 'sdfghjhkl;' + 'xcvbnm,./'
    d = {' ': ' '}

    for k, v in zip(r2, r1):
        d[k.upper()] = v.upper()
    word = par
    result = []
    for c in word:
        result.append(d[c])
    return ''.join(result)


class Solver:

    def getInput(self):
        self.numOfTests = 1
        self.input = []
        word = self.fIn.readline().strip()
        self.input.append((word))

    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
        self.results = []

    def parallel(self):
        self.getInput()
        p = Pool(4)
        millis1 = int(round(time.time() * 1000))
        self.results = p.map(solve, self.input)
        millis2 = int(round(time.time() * 1000))
        print("Time in milliseconds: %d " % (millis2 - millis1))
        self.makeOutput()

    def sequential(self):
        self.getInput()
        millis1 = int(round(time.time() * 1000))
        for i in self.input:
            self.results.append(solve(i))
        millis2 = int(round(time.time() * 1000))
        print("Time in milliseconds: %d " % (millis2 - millis1))
        self.makeOutput()

    def makeOutput(self):
        for test in range(self.numOfTests):
            self.fOut.write("Case #%d: %s\n" % (test + 1, self.results[test]))
        self.fIn.close()
        self.fOut.close()

if __name__ == '__main__':
    solver = Solver()
    if parallelSolve:
        solver.parallel()
    else:
        solver.sequential()
