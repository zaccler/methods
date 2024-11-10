class RealString:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __lt__(self, other):
        return len(self) < len(other)
    
    def __on__(self, other):
        return len(self) == len(other)
    

str1 = RealString(input("Первая строка: "))
str2 = RealString(input("Вторая строка: "))

print(f"1-ая больше 2-ой: {str1 > str2}")
print(f"1-ая меньше 2-ой: {str1 < str2}")
print(f"они равны: {str1 == str2}")