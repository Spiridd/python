def main(secret):
    # invariant: secret in [a, b)
    a, b = 1, 1001
    while a < b-1:
        # print('[{} {})'.format(a, b))
        m = (a+b)//2
        if secret >= m:
            a = m
        else:
            b = m
    return a


for n in range(1, 1000+1):
    if n != main(n):
        print('fuck this number! %s' % n)
print('end')
