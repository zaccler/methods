class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def get_kg(self):
        return self.__kg

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

    kg = property(get_kg, set_kg, doc="Свойство для работы с килограммами")
    pounds = property(to_pounds, doc="Свойство для получения веса в фунтах")



try:
    kg_input = float(input("Введите вес в килограммах: "))
    weight = KgToPounds(kg_input)
    print(f"{weight.kg} кг = {weight.pounds:.2f} фунтов")
except ValueError as e:
    print(f"Ошибка: {e}")
