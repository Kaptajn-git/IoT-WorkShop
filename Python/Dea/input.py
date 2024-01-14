
#input() er en indbygget funktion i Python, der bruges til at få input fra brugeren via tastaturet.
#Når input() kaldes, stopper programmet, og det venter på, at brugeren skriver noget og trykker på Enter.
#Den indtastede tekst returneres som en streng (string), som du normalt gemmer i en variabel for senere brug.

bruger_input = input("Indtast noget: ")
print("Du indtastede:", bruger_input)

#I dette eksempel bruger input()-funktionen brugeren til at indtaste noget, og den indtastede værdi gemmes i variablen bruger_input.
#Derefter udskrives den indtastede værdi.

#Vær opmærksom på, at input() altid returnerer en streng.
#Hvis du har brug for et heltal eller en anden datatype, skal du konvertere det manuelt ved hjælp af int(), float(), osv.

alder = int(input("Hvor gammel er du? "))

#Her konverteres brugerens input til et heltal ved hjælp af int().
#Hvis brugeren indtaster noget, der ikke kan konverteres til et heltal, vil programmet kaste en fejl.
#Derfor er det en god idé at håndtere fejl ved at bruge try-except blokke,isnumeric() eller lignende, hvis du forventer brugerens input af en bestemt type.