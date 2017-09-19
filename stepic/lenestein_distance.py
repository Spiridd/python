"""
Вычислите расстояние редактирования двух данных непустых
строк длины не более 102102, содержащих строчные буквы латинского алфавита.
"""
# O(nm) complexity
# O(nm) memory
# dynamic programming: Top Down


def levenstein_distance(s1, s2):
    d = [[-1 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

    def diff(i, j):
        return 1 if s1[j-1] != s2[i-1] else 0

    def edit_distance(i, j):
        if d[i][j] < 0:
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            else:
                del_cost = edit_distance(i, j-1) + 1
                sub_cost = edit_distance(i-1, j-1) + diff(i, j)
                ins_cost = edit_distance(i-1, j) + 1
                d[i][j] = min(ins_cost, del_cost, sub_cost)
        return d[i][j]

    return edit_distance(len(s2), len(s1))


def main():
    string1 = input()
    string2 = input()
    distance = levenstein_distance(string1, string2)
    print(distance)


if __name__ == '__main__':
    main()
