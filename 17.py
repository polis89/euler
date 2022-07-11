import time

start = time.time()

# START

counts = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "onethousand"
}

def printNumber(number):
    if len(str(number)) == 3:
        hundreds = number // 100
        if number % 100 != 0:
            return counts[hundreds] + counts[100] + "and" + printNumber(number % 100)
        return counts[hundreds] + counts[100]
    if number in counts:
        return counts[number];
    tenth = number // 10
    return counts[tenth * 10] + counts[number % 10]

count = 0

for i in range(1,1001):
    count += len(printNumber(i))

print(count)

# END

end = time.time()
print(f'time: {end - start}')