import random
import time


class Cell:

    def __init__(self):
        pass


class field:
    def __init__(self, m, n):
        self.list1, self.list2 = [], []
        self.m, self.n = m, n


    def __iter__(self):
        return self


    def gender(self):
        for i in range(self.m):
            self.list2.append([None] * n)
        for i in range(self.m):
            for j in range(self.n):
                rand = random.random()
                if rand < 0.10:
                    # "\033[31m M"
                    self.list2[i][j] = Maniac()
                elif rand < 0.25:
                    # "\033[35m F"
                    self.list2[i][j] = Frank()
                elif rand < 0.60:
                    # "\033[32m L"
                    self.list2[i][j] = Civilian()
                else:
                    # "\033[37m *"
                    self.list2[i][j] = DeadCell()

        for x in self.list2:
            print(*x)
        print()
        self.list1 = self.list2.copy()

    def __next__(self):
        for i in range(self.m):
            for j in range(self.n):
                self.i, self.j = i, j
                if isinstance(self.list1[i][j], Frank):
                    self.list1[i][j].Morgenshtern(self)

        for i in range(self.m):
            for j in range(self.n):
                self.i, self.j = i, j
                if isinstance(self.list1[i][j], Civilian):
                    self.list1[i][j].Civa(self)

        for i in range(self.m):
            for j in range(self.n):
                self.i, self.j = i, j
                if isinstance(self.list1[i][j], DeadCell):
                    self.list1[i][j].suicideboys(self)

        for i in range(self.m):
            for j in range(self.n):
                self.i, self.j = i, j
                if isinstance(self.list1[i][j], Maniac):
                    self.list1[i][j].Chertila(self)

        self.list1 = self.list2.copy()
        return self.list1


class DeadCell(Cell):

    def __str__(self):
        return "\033[37m *"

    def suicideboys(self, field):
        p = 0
        m, n = field.m - 1, field.n - 1
        if (field.i - 1 >= 0 and field.j - 1 >= 0) and not isinstance(field.list1[field.i - 1][field.j - 1], DeadCell):
            p += 1
        if field.j - 1 >= 0 and not isinstance(field.list1[field.i][field.j - 1], DeadCell):
            p += 1
        if (field.i - 1 >= 0 and field.j + 1 <= n) and not isinstance(field.list1[field.i - 1][field.j + 1], DeadCell):
            p += 1
        if field.i - 1 >= 0 and not isinstance(field.list1[field.i - 1][field.j], DeadCell):
            p += 1
        if field.i + 1 <= m and not isinstance(field.list1[field.i + 1][field.j], DeadCell):
            p += 1
        if (field.i + 1 <= m and field.j + 1 <= n) and not isinstance(field.list1[field.i + 1][field.j + 1], DeadCell):
            p += 1
        if field.j + 1 <= n and not isinstance(field.list1[field.i][field.j + 1], DeadCell):
            p += 1
        if (field.i + 1 <= m and field.j - 1 >= 0) and not isinstance(field.list1[field.i + 1][field.j - 1], DeadCell):
            p += 1

        if p >= 3:
            rand = random.random()
            if rand < 0.10:
                field.list2[field.i][field.j] = Maniac()
            elif rand < 0.25:
                field.list2[field.i][field.j] = Frank()
            elif rand < 0.60:
                field.list2[field.i][field.j] = Civilian()


class Civilian(Cell):

    def __str__(self):
        return "\033[32m L"

    def Civa(self, field):
        p = 0
        m, n = field.m - 1, field.n - 1
        if (field.i - 1 >= 0 and field.j - 1 >= 0) and not isinstance(field.list1[field.i - 1][field.j - 1], DeadCell):  ## наискосок вверх и налево
            p += 1
        if field.j - 1 >= 0 and not isinstance(field.list1[field.i][field.j - 1], DeadCell):  ## влево
            p += 1
        if (field.i - 1 >= 0 and field.j + 1 <= n) and not isinstance(field.list1[field.i - 1][field.j + 1], DeadCell):  ## наискосок вверх и направо
            p += 1
        if field.i - 1 >= 0 and not isinstance(field.list1[field.i - 1][field.j], DeadCell):  ## вверх
            p += 1
        if field.i + 1 <= m and not isinstance(field.list1[field.i + 1][field.j], DeadCell):  ## вниз
            p += 1
        if (field.i + 1 <= m and field.j + 1 <= n) and not isinstance(field.list1[field.i + 1][field.j + 1], DeadCell):  ## наискосок вниз и вправо
            p += 1
        if field.j + 1 <= n and not isinstance(field.list1[field.i][field.j + 1], DeadCell):  ## вправо
            p += 1
        if (field.i + 1 <= m and field.j - 1 >= 0) and not isinstance(field.list1[field.i + 1][field.j - 1], DeadCell):  ## наискосок вниз налево
            p += 1

        if p != 2 and p != 3:
            field.list2[field.i][field.j] = DeadCell()


class Maniac(Cell):

    def __str__(self):
        return "\033[31m M"

    def Chertila(self, field):
        p = 0
        m, n = field.m - 1, field.n - 1
        rand = random.random()
        if (field.i - 1 >= 0 and field.j - 1 >= 0) and not isinstance(field.list1[field.i - 1][field.j - 1],
                                                                      DeadCell):  ##верх и налево
            if rand < 0.25:
                field.list2[field.i - 1][field.j - 1] = DeadCell()
        else:
            p += 1
        if field.j - 1 >= 0 and not isinstance(field.list1[field.i][field.j - 1], DeadCell):  ##влево
            if rand < 0.25:
                field.list2[field.i][field.j - 1] = DeadCell()
        else:
            p += 1
        if (field.i - 1 >= 0 and field.j + 1 <= n) and not isinstance(field.list1[field.i - 1][field.j + 1], DeadCell):  ## вверх направо
            if rand < 0.25:
                field.list2[field.i - 1][field.j + 1] = DeadCell()
        else:
            p += 1
        if field.i - 1 >= 0 and not isinstance(field.list1[field.i - 1][field.j], DeadCell):  ## вверх
            if rand < 0.25:
                field.list2[field.i - 1][field.j] = DeadCell()
        else:
            p += 1
        if field.i + 1 <= m and not isinstance(field.list1[field.i + 1][field.j], DeadCell):  ## вниз
            if rand < 0.25:
                field.list2[field.i + 1][field.j] = DeadCell()
        else:
            p += 1
        if (field.i + 1 <= m and field.j + 1 <= n) and not isinstance(field.list1[field.i + 1][field.j + 1], DeadCell):  ## вниз вправо
            if rand < 0.25:
                field.list2[field.i + 1][field.j + 1] = DeadCell()
        else:
            p += 1
        if field.j + 1 <= n and not isinstance(field.list1[field.i][field.j + 1], DeadCell):  ## вправо
            if rand < 0.25:
                field.list2[field.i][field.j + 1] = DeadCell()
        else:
            p += 1
        if (field.i + 1 <= m and field.j - 1 >= 0) and not isinstance(field.list1[field.i + 1][field.j - 1], DeadCell):  ## вниз налево
            if rand < 0.25:
                field.list2[field.i + 1][field.j - 1] = DeadCell()
        else:
            p += 1

        if p == 8:
            field.list2[field.i][field.j] = DeadCell()


class Frank(Cell):
    def __str__(self):
        return "\033[35m F"
    def Morgenshtern(self, field):
        p = 0
        m, n = field.m - 1, field.n - 1
        ran = random.random()
        if (field.i - 1 >= 0 and field.j - 1 >= 0) and isinstance(field.list1[field.i - 1][field.j - 1],DeadCell):  ##верх и налево
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list2[field.i - 1][field.j - 1] = Maniac()
                elif rand < 0.25:
                    field.list2[field.i - 1][field.j - 1] = Frank()
                else:
                    field.list2[field.i - 1][field.j - 1] = Civilian()
        else:
            p += 1

        if field.j - 1 >= 0 and isinstance(field.list1[field.i][field.j - 1], DeadCell):  ##влево
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i][field.j - 1] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i][field.j - 1] = Frank()
                else:
                    field.list1[field.i][field.j - 1] = Civilian()
        else:
            p += 1

        if (field.i - 1 >= 0 and field.j + 1 <= n) and isinstance(field.list1[field.i - 1][field.j + 1],DeadCell):  ## вверх направо
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i - 1][field.j + 1] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i - 1][field.j + 1] = Frank()
                else:
                    field.list1[field.i - 1][field.j + 1] = Civilian()
        else:
            p += 1

        if field.i - 1 >= 0 and isinstance(field.list1[field.i - 1][field.j], DeadCell):  ## вверх
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i - 1][field.j] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i - 1][field.j] = Frank()
                else:
                    field.list1[field.i - 1][field.j] = Civilian()
        else:
            p += 1
        if field.i + 1 <= m and isinstance(field.list1[field.i + 1][field.j], DeadCell):  ## вниз
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i + 1][field.j] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i + 1][field.j] = Frank()
                else:
                    field.list1[field.i + 1][field.j] = Civilian()
        else:
            p += 1
        if (field.i + 1 <= m and field.j + 1 <= n) and isinstance(field.list1[field.i + 1][field.j + 1],DeadCell):  ## вниз вправо
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i + 1][field.j + 1] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i + 1][field.j + 1] = Frank()
                else:
                    field.list1[field.i + 1][field.j + 1] = Civilian()
        else:
            p += 1
        if field.j + 1 <= n and isinstance(field.list1[field.i][field.j + 1], DeadCell):  ## вправо
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i][field.j + 1] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i][field.j + 1] = Frank()
                else:
                    field.list1[field.i][field.j + 1] = Civilian()
        else:
            p += 1
        if (field.i + 1 <= m and field.j - 1 >= 0) and isinstance(field.list1[field.i + 1][field.j - 1],DeadCell):  ## вниз налево
            if ran < 0.20:
                rand = random.random()
                if rand < 0.10:
                    field.list1[field.i + 1][field.j - 1] = Maniac()
                elif rand < 0.25:
                    field.list1[field.i + 1][field.j - 1] = Frank()
                else:
                    field.list1[field.i + 1][field.j - 1] = Civilian()
        else:
            p += 1

        if p == 8:
            field.list2[field.i][field.j] = DeadCell()


m, n = 20, 20
matrix = field(m, n)
matrix.gender()
for m in matrix:
    for i in m:
        print(*i)
    print()
    time.sleep(1)
