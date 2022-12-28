class Point:
    def __init__(self, x = 0, y = 0):
        self.q = x
        self.w = y
        print("Создание экземпляра класса point")

    def __del__(self):
        print("Удаление экземпляра" + self.__str__())
    x = 1; y = 1
    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt = Point(5,10)
print(pt.__dict__)

