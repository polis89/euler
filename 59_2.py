import time
from utils import xor, num2ascii

start = time.time()

# START

# candidates
# '88,4,13': 17   key: 44,108,104
# '69,12,24': 15   key: 40,100,125
# '13,29,80': 14   key: 121,117,53
# '4,13,29': 14   key: 112,101,120
# print(f't: {xor(116,4)}')
# print(f'h: {xor(104,13)}')
# print(f'e: {xor(101,29)}')

result = ""
key = [101,120,112]
cur_key_index = 0
summ = 0

with open('p059_cipher.txt', 'r') as f:
    for line in f:
        letters = line.split(',')
        for i in range(0, len(letters)):
            decripted_letter = num2ascii(xor(int(letters[i]),key[cur_key_index]))
            summ += ord(decripted_letter)
            result += decripted_letter
            cur_key_index = (cur_key_index + 1) % 3

print(result)
print(summ)


# END

end = time.time()
print(f'time: {end - start}')