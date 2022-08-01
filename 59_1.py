import time

start = time.time()

# START

letter_dict = dict()

with open('p059_cipher.txt', 'r') as f:
    for line in f:
        letters = line.split(',')
        for i in range(2, len(letters)):
            key = letters[i-2] + ',' + letters[i-1] + ',' + letters[i]
            if key in letter_dict:
                letter_dict[key] += 1
            else:
                letter_dict[key] = 1

# candidates
# '88,4,13': 17
# '69,12,24': 15
# '13,29,80': 14
# '4,13,29': 14

sorted_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

# END

end = time.time()
print(f'time: {end - start}')