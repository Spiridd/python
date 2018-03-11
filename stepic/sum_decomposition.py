n = int(input())
terms = []
term = 1
while n > 0:
    if n-term > term or n == term:
        n -= term
        terms.append(term)
    term += 1
print(len(terms))
[print(term, end=' ') for term in terms]
