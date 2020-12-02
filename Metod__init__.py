class Student:
#атрибуты
    name='unknow'
    age=0
   
#методы
    def add_Name(self, x):
        self.name=x
    def add_Age(self, x):
        self.age=x
    def display(self):
        print('Name: {} \nAge: {}'.format(self.name, self.age))

#объекты
newObject=Student()
newObject.add_Name(input('name '))
newObject.add_Age(input('age '))
newObject.display()


class Student2:
#атрибуты
    name='unknow'
    age=0
   
#методы
    def __init__(self, x, y):
        self.name=x
        self.age=y
    def display(self):
        print('Name: {} - Age: {}'.format(self.name, self.age))
#объекты
newObject=Student2(input('Name '),input('age '))
newObject.display()


class Student3:
#атрибуты
    name=course='unknow'
    age=0
   
#методы
    def __init__(self, x, y, g):
        self.name=x
        self.age=y
        self.course=g
    def display(self):
        print('Name: {} - Age: {} - Course: {}'.format(self.name, self.age, self.course))
#объекты
newObject=Student3(input('Name '),input('age '),input('Course'))
newObject.display()


class Car:
#атрибуты
    brand=color='unknow'
    year=maxspeed=price=0
#методы
    def __init__(self,x,y,z,g,h):
        self.brand=x
        self.year=y
        self.price=z
        self.color=g
        self.maxspeed=h
    def display(self):
        print('Brand: {} - Year: {} - Price: {} - Color: {} - MaxSpeed: {}'.format(self.brand, self.year, self.price, self.color, self.maxspeed))
#объекты
newObject1=Car(input('Fiat Brand '),input('Fiat Year '),input('Fiat Price'),input('Fiat Color '),input('Fiat MaxSpeed'))
newObject1.display()
newObject2=Car(input('Lada Brand '),input('Lada Year '),input('Lada Price'),input('Lada Color '),input('Lada MaxSpeed'))
newObject2.display()      
       