class Nikola:
    __slots__ = ['name', 'age']  # Ограничение на создание дополнительных атрибутов

    def __init__(self, name, age):
        self.age = age
        
        self.name = name if name == "Николай" else f"Я не {name}, а Николай"


name_input = input("Введите имя: ")
age_input = int(input("Введите возраст: "))

# Создание экземпляра класса Nikola
person = Nikola(name_input, age_input)


print(person.name)
print(person.age)
