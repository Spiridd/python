def isprime(p):
    for div in range(2, int(p**0.5)+1):
        if p % div == 0:
            return False
    return True


def primes():
    yield 2
    p = 3
    while True:
        if isprime(p):
            yield p
        p += 2


class multifilter_stepic:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = tuple(func for func in funcs)
        self.judge = judge

    def __iter__(self):
        for item in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(item):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield item


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.filtered = []
        for item in iterable:
            pos = 0
            neg = 0
            for func in funcs:
                if func(item):
                    pos += 1
                else:
                    neg += 1
            if judge(pos, neg):
                self.filtered.append(item)

    def __iter__(self):
        return iter(self.filtered)


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]
m = multifilter(a, mul2, mul3, mul5)
print(list(m))

m = multifilter_stepic(a, mul2, mul3, mul5)
print(list(m))

gen = primes()
print(next(gen))
print(next(gen))
