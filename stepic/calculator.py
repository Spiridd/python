"""
У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
заменить x на 2x, 3x или x+1. По данному целому числу 1≤n≤10^5 определите
минимальное число операций k, необходимое, чтобы получить n из 1.
Выведите k и последовательность промежуточных чисел.
"""
# Bottom Up


def get_sequence(n):
    sequence = {1: 0}
    for i in range(1, n+1):
        double = 2 * i
        try:
            sequence[double] = min(sequence[double], sequence[i]+1)
        except KeyError:
            sequence[double] = sequence[i]+1
        triple = 3 * i
        try:
            sequence[triple] = min(sequence[triple], sequence[i]+1)
        except KeyError:
            sequence[triple] = sequence[i]+1
        plus_one = 1 + i
        try:
            sequence[plus_one] = min(sequence[plus_one], sequence[i]+1)
        except KeyError:
            sequence[plus_one] = sequence[i]+1

    inters = []
    num = n
    prev = n+1
    operations = sequence[num]
    for _ in range(sequence[n]):
        while sequence[num] != operations or (prev != num*3 and prev != num*2 and prev != num+1):
            num -= 1
        inters.append(num)
        prev = num
        num -= 1
        operations -= 1
    inters.append(1)

    return reversed(inters), len(inters)-1


def main():
    n = int(input())
    sequence, count = get_sequence(n)
    print(count)
    [print(s, end=' ') for s in sequence]


if __name__ == '__main__':
    main()
