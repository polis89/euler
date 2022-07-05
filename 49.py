from utils import isPrime, getPermutationsNumber

primes = dict()

for x in range(1001, 10000, 2):
  if isPrime(x):
    primes[x] = set()

for prime in primes:
    permutations = getPermutationsNumber(prime)
    print(f'\nprime: {prime}')
    for permutation in permutations:
        if permutation != prime and permutation in primes:
            primes[prime].add(permutation)

print(f'before: {len(primes)}')

filteredPrimes = [x for x in primes if len(primes[x]) > 1]

for prime in primes:
    if len(primes[prime]) < 2:
        continue
    for prime2 in primes[prime]:
        diff = prime2 - prime
        if (prime2 + diff) in primes[prime]:
            print(f'FOUND: {prime} {prime2} {prime2 + diff}')
            break

print(f'after: {len(filteredPrimes)}')