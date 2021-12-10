class MyClass:
    zahl = 15
    buchstaben = "abc"
    list = [] #Verändert sich für alle Instanzen

    def say_hello(self, name):
        print("hello" + name)
        self.zahl += 10  # Zugriff auf Variable innerhalb der Klasse
    def __init__(self, pluszahl= 0):
        self.test = 123 + pluszahl

int = MyClass(100)

int.say_hello("Tim")
print(int.test)