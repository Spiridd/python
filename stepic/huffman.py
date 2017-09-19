from heapq import heapify, heappop, heappush
from collections import Counter


def encode(sym2freq):
    if len(sym2freq) == 1:
        return [[list(sym2freq.keys())[0], '0']]
    heap = [[wt, [sym, '']] for sym, wt in sym2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [left[0]+right[0]] + left[1:] + right[1:])
    return heappop(heap)[1:]


text = input()
freq = Counter(text)
huff = encode(freq)
letter_code = {}
for pair in huff:
    letter_code[pair[0]] = pair[1]
code_size = 0
for letter, code in letter_code.items():
    code_size += freq[letter]*len(code)
print(len(freq), code_size)
for letter, code in letter_code.items():
    print('{}: {}'.format(letter, code))
for letter in text:
    print(letter_code[letter], end='')
