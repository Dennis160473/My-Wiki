# Programmierübungen


# Aufgabe 1
def calc_area(width, height):
    return width * height


width = float(input("Please enter a number? "))
height = float(input("Please enter a number? "))

if calc_area(width, height):
    print(f"Das Ergebnis der Fläche ist {width * height}.")
else:
    print()


# Aufgabe 2
print("Meilen <-> Kilometer")
faktor = 1.60934

print("(1) Meilen -> Kilometer")
print("(2) Kilometer -> Meilen")
print("(3) Beenden")
auswahl = int(input("Deine Wahl: "))

if auswahl == 1:
    s = float(input("Strecke in Meilen: "))
    s = s / faktor
    print(f"Das sind {s}= Kilometer")
elif auswahl == 2:
    s = float(input("Strecke in Kilometern: "))
    s = s * faktor
    print(f"Das sind {s}= Meilen")
else:
    print("Diese Eingabe war nicht vorgesehen")

print("Ende des Programms")


# Hit import statements
from datetime import datetime
import random

now = datetime.now()
print(now)
print(random.randint)


# Vorgefertigte Pakete in Python
import datetime

date_str = "2024-12-24"
date = datetime.datetime(2024, 12, 24)
date.year


# Algorithmus anwenden
def kaffee_kochen():
    print("Wasser erhitzen")
    print("Kaffeepulver in die Maschine geben")
    print("Wasser einfüllen")
    print("Maschine einschalten")
    print("Kaffee genießen")


kaffee_kochen()


zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])


# Aufgabe 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sum(list)
print(result)


def summe():
    result = 0
    for nr1 in list:
        result = result + nr1
        return result


print(f"Summe der Liste {summe()}")



## Listen werden immer mit [] initialisiert
name_list = ["Christof", "Mete", "Joshua", "Nassima", "Sebastian"]
# Element in einer Liste können über Indizes abgerufen werden
# In der Liste oben gibt es index 0 --> "Christof" name_list[0]
# index 1 --> "Mete"
# index 2 --> "Joshua"
print(f"Das erste Element ist: {name_list[0]}")
print(f"Das zweite Element ist: {name_list[1]}")
print(f"Das dritte Element ist: {name_list[2]}")
print(f"Das 4. Element ist: {name_list[3]}")
print(f"Das 5. Element ist: {name_list[-1]}")
print(f"Die geamte Liste sieht so aus: {name_list}")
for i in range(len(name_list)):
    print(f"Das {i}. Element ist aus dem Loop: {name_list[i]}")
for n in name_list:
    print(f"Element ist aus neuen dem For-Loop ist: {n}")

### dictionarya
#### Die Initialisierung startet mit {}
#### besteht aus key, value pair "<key>: "<value>"
#### Der value ist ein beliebiger Datentyp
score_dict = {}
# key value Pair einfügen
score_dict = ["max"] = 100
# wert zu einem key aufrufen
score_max = score_dict = ["max"] # 100
print (f"{score_max}")


score_dict = ["anna"] = 80
score_anna = score_dict["anna"]
print(f"{score_anna}")


for key in score_dict.keys(): # ["max", "anna"]
    print(f"{key}")

for v in score_dict.value(): # [100, 80]
    print(f"{v}")

for k, value in score_dict.items():
    print(f"Key{k}, {value}")



class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tank_volume,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank_volume = tank_volume

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def get_nr_of_tanks(self):
        distance_with_one_tank = self.consumption * self.tank_volume = 1000 # 1000km
        # (100l / 10l/100km = 10l) * 100l = 1000km
        return self.km_driven / distance_with_one_tank

my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
my_vehicle.use_tank()
my_vehicle.get_nr_of_tanks()
print(f"The total consumption is: {my_vehicle.get_total_consumption()}")
print(f" The car needs {my_vehicle.get_nr_of_tanks()} tanks to cover a distance of 1000km.")