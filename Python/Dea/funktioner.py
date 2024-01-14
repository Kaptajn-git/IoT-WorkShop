#Funktioner er en måde hvorpå vi kan genbruge kode. F.eks. hvis vi skal gøre det samme flere gange.

# definer en funktion
def hello_world():
    print("Hello World")

# kald funktionen
hello_world()

# output er "Hello World"


#En funktion kan også tage imod parametre.

# definer en funktion, der tager imod en parameter

def hello(name):
    print(f"Hej {name} har du en dejlig dag?")

# kalder funktionen med en parameter, her en String med værdien "Mikkel".
hello("Mikkel")

# output er "Hello Mikkel"

def hilsen(navn):
    """Denne funktion udskriver en hilsen."""
    print("Hej, " + navn + "!")

# Kald funktionen og passer en parameter
hilsen("Alice")
