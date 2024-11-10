class TriangleChecker:
    def __init__(self, *sides):
        # преобразуем данные  список
        try:
            self.sides = list(map(float, sides))
        except ValueError:
            self.sides = None

    def is_triangle(self):
        # Проверка входных данных на числоые значения
        if self.sides is None:
            return "Нужно вводить только числа!"

        # Проверка, что все стороны положительные
        if any(side <= 0 for side in self.sides):
            return "ничего не буду делать, отрицательные числа!"

        # Проверка на возможность создания треугольника
        a, b, c = self.sides
        if a + b > c and a + c > b and b + c > a:
            return "можно построить треугольник!"
        else:
            return "треугольник не сделать, ты не то ввёл."


stroki = input("введи стороны трегольника: ")
stroki = stroki.split()

triangle1 = TriangleChecker(*stroki)
print(triangle1.is_triangle())

