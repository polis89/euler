import time
from utils import gcd, isPrime

start = time.time()

# START

target_resilience = 15499 / 94744
# target_resilience = 4/10

primes = []
for i in range(2, 1000):
    if isPrime(i):
        primes.append(i)

current_denominator = 2
current_found_resilients = 1
latest_taken_prime = 0

while True:
    latest_taken_prime += 1
    current_denominator *= primes[latest_taken_prime]
    current_found_resilients *= (primes[latest_taken_prime] - 1)
    resilience = current_found_resilients / (current_denominator - 1)

    print(f'for denominator {current_denominator} found resilients: {current_found_resilients}. Resilience: {resilience}')

    if resilience < target_resilience:
        print("=========================")
        best_solution = current_denominator
        best_resilience = resilience

        step = int(current_denominator / primes[latest_taken_prime])

        current_found_resilients = int(current_found_resilients / (primes[latest_taken_prime] - 1))
        resilients_step = current_found_resilients
        for test_value in range(2*step, current_denominator, step):
            current_denominator = test_value
            current_found_resilients += resilients_step 
            resilience = current_found_resilients / (current_denominator - 1)
            print(f'for denominator {current_denominator} found resilients: {current_found_resilients}. Resilience: {resilience}')
            if resilience < target_resilience:
                print(f'solution: {test_value}')
                break
        break


# lowest_resilience = 1
# step = 210
# current_denominator = 210
# print(f'step: {step}')

# while True:
#     resilient_count = 1
#     max_resilient_count = lowest_resilience * (current_denominator - 1) + 1
#     collected_dividers = []
#     for i in range(2, current_denominator):
#         continue_flag = False
#         for d in collected_dividers:
#             if i % d == 0:
#                 continue_flag = True
#                 break
#         if continue_flag:
#             continue
#         if gcd(i, current_denominator) == 1:
#             resilient_count += 1
#             # if resilient_count > max_resilient_count:
#             #     break
#         else:
#             collected_dividers.append(i)
#     resilience = resilient_count / (current_denominator - 1)
#     if resilience < target_resilience:
#         print(f'SOLVED: {current_denominator}')
#         break
#     print(f'for denominator {current_denominator} found resilients: {resilient_count}. Resilience: {resilience}')
#     if resilience < lowest_resilience:
#         lowest_resilience = resilience
#     # if step * primes[last_taken_prime + 1] <= current_denominator:
#     #     last_taken_prime += 1
#     #     current_denominator = current_denominator * primes[last_taken_prime]
#     #     step = step * primes[last_taken_prime]
#     #     print(f'step: {step}')
#     if current_denominator > 3000:
#         break
#     current_denominator += step

# list_of_primes = []

# while True:
#     if isPrime(current_denominator):
#         list_of_primes.append(current_denominator)
#     numerators = range(1, current_denominator)
#     for prime in list_of_primes:
#         if current_denominator != prime and current_denominator % prime == 0:
#             numerators = [0 if v % prime == 0 else v for v in numerators]
#             # non_resilient_count += (current_denominator // prime) - 1
    
#     resilient_count = len([v for v in numerators if v != 0])
#     resilience = resilient_count / (current_denominator - 1)
#     # print(f'for denominator {current_denominator} found resilients: {resilient_count}. Resilience: {resilience}')
#     # print(numerators)
#     if resilience < target_resilience:
#         print(f'SOLVED: {current_denominator}')
#         print(f'resilient_count: {resilient_count}')
#         break
#     if resilience < lowest_resilience:
#         lowest_resilience = resilience
#         print(f'LOWEST: {current_denominator}. remains to targer: {lowest_resilience - target_resilience}')
#     # if current_denominator > 10000:
#     #     break
#     current_denominator += 1



# best time to 10000: 13.876221656799316
# best time to 10000: 10.56

# END

end = time.time()
print(f'time: {end - start}')