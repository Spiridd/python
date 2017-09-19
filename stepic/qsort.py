'''
minimalistic implementation of quick sort
show only 4 times slower performance
than inner sort (timsort)
'''
import random


def qsort(v):
    return qsort([x for x in v[1:] if x < v[0]]) + [v[0]] +\
            qsort([x for x in v[1:] if x >= v[0]]) \
            if len (v) > 1 else v


def main():
    size = 1000000
    vec = random.sample(range(size), size)
    #vec.sort()
    vec = qsort(vec)


if __name__ == '__main__':
    main()

