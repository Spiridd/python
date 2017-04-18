class Buffer:
    def __init__(self):
        self.vec = []

    def add(self, *a):
        self.vec = self.vec + list(a)
        while len(self.vec) >= 5:
            print(sum(self.vec[:5]))
            self.vec = self.vec[5:]

    def get_current_part(self):
        return self.vec


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())  # вернуть [1]
