import math
import itertools

def isPrime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False

    for x in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False

    return True

def getPermutationsNumber(num):
    digits = [int(a) for a in str(num)]
    return [int(''.join(map(str,x))) for x in list(itertools.permutations(digits))]

def isPermutation(a,b):
    aSplitted = [int(x) for x in str(a)]
    bSplitted = [int(x) for x in str(b)]
    if len(aSplitted) != len(bSplitted):
        return False
    for x in aSplitted:
        if x not in bSplitted:
            return False
        bSplitted.remove(x)
    return True