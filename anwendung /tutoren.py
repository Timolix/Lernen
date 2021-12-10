
def say_hello():
    print("hello")


class Tutor:

    def __init__(self, name, alter, fach1, fach2, fach3):
        self.name_tutor = name
        self.alter_tutor = str(alter)
        self.fach_1 = fach1
        self.fach_2 = fach2
        self.fach_3 = fach3

    def vorstellen(self):
        print("Hallo mein Name ist " + self.name_tutor + " und ich bin " + self.alter_tutor + " Jahre alt.")
        print("Zu meinen Fächern gehören " + self.fach_1 + ", " + self.fach_2 + " und " + self.fach_3 +".")


class Minijober(Tutor):
    sozialabgaben = 1 - 0.36
    max_stunden_woche = 9

    def vorstellen_minijobber(self):
        Tutor.vorstellen(self)
        print("Ich arbeite auf Minijob-Basis.")

class Werkstudent(Tutor):
    sozialabagen = 0
    min_stunden_wochen = 9
    max_stunden_wochen = 20

taha_kassabi = Minijober("Taha Kassabi", 19, "Mathematik", "Informatik", "Englisch")


#tim_pietrowski = Tutor("Tim Pietrowski", 19, "Mathematik", "Physik", "Deutsch")

#tim_pietrowski.vorstellen()



