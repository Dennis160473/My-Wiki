# Grundlagen
## Datentypen
###Variablen können Daten unterschiedlichen Typs speichern und unterschiedliche Typen können unterschiedliche Dinge tun.
###Python hat die folgenden Datentypen in diesen Kategorien standardmäßig integriert:
# Texttyp:	str - x = "Hello World"
# Numerische Typen:	int, float, complex - x = 111, x = 32,2, x = 1j
# Sequenztypen:	list, tuple, range - x = ["apple", "banana", "cherry"], x = ("apple", "banana", "cherry"), x = range(6)
# Zuordnungstyp:	dict - x = {"name" : "John", "age" : 36}
# Typen festlegen:	set,frozenset - x = {"apple", "banana", "cherry"}, x = frozenset({"apple", "banana", "cherry"})
# Boolescher Typ:	bool - x = True
# Binäre Typen:	bytes, bytearray, memoryview - x = b"Hello", x = bytearray(5), x = memoryview(bytes(5))
# Keiner Typ:	NoneType - x = None

### Um den Typ eines beliebigen Objekts in Python zu überprüfen, verwenden Sie die type()Funktion:
z = 1j
print(type(z))

### Python verfügt nicht über eine random()Funktion zum Generieren von Zufallszahlen, hat aber ein integriertes Modul namens random, mit dem Zufallszahlen generiert werden können.
# Importieren Sie das Zufallsmodul und zeigen Sie eine Zufallszahl von 1 bis 9 an.
import random

print(random.randrange(1, 10))
