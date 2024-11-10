
class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def showMyDrink(self):
        if self.additive:
            print(f"Газировка с {self.additive}")
        else:
            print("Обычная газировка")


drink1 = Soda("лимоном")
drink1.showMyDrink()   

drink2 = Soda()
drink2.showMyDrink()  