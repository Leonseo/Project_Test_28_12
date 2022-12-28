"""Класс для представления автомобиля."""
class Car():
     '''простая модель автомобиля'''

     def __init__(self,make, model, year):
         '''Инициализирует атрибуты описания автомобиля.'''
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0


     def get_descriptive_name(self):
         '''Инициализирует атрибуты описания автомобиля.'''
         long_name = f"{self.year} {self.make} {self.model}"
         return long_name


     def read_odometer(self):
         '''Выводит пробег машины в милях.'''
         print(f"Эта машина имеет пробег - {self.odometer_reading} милей")


     def update_odometer(self, mileage):
         '''Устанавливает на одометре заданное значение.
         Устанавливает на одометре заданное значение.'''
         if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
         else:
             print("Нельзя скручивать пробег!")


     def increment_odometer(self, miles):
         '''Устанавливает на одометре заданное значение.'''
         self.odometer_reading += miles


class Battery():
    '''Простая модель аккумулятора электромобиля.'''


    def __init__(self, battery_size=75):
        '''Инициализация атрибутов аккумулятора.'''
        self.battery_size = battery_size


    def describe_battery(self):
        '''Выводит информацию о мощности аккумулятора.'''
        print(f"Эта машина с батареей в {self.battery_size}-kWh ")


    def get_range(self):
        '''Выводит приблизительный запас хода для аккумулятора.'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Эта машина имеет приблизительный запас хода - {range}")


class ElectricCar(Car):
    '''Представляет аспекты машины, специфические для электромобилей.'''


    def __init__(self, make, model, year):
        '''Инициализирует атрибуты класса-родителя.
        Инициализирует атрибуты класса-родителя.'''
        super().__init__(make,model,year)
        self.battery = Battery()