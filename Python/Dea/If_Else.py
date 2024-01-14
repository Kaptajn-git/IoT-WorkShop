
#if og else er betingede udsagn i Python, der bruges til at udføre forskellige handlinger afhængigt af, om en given betingelse er sand eller falsk.

#Hvis betingelsen er sand, udføres blokken under if.
#Hvis betingelsen er falsk, udføres blokken under else (hvis der er en else-del).

alder = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er myndig.")
else:
    print("Du er ikke myndig endnu.")
    
    
#I dette eksempel tjekker programmet om brugerens alder er 18 eller derover.
#Hvis det er tilfældet, udskrives "Du er myndig."
#Hvis det ikke er tilfældet, udskrives "Du er ikke myndig endnu."

#Du kan også have flere if-udsagn efter hinanden (uden else), hvis du ønsker at evaluere flere betingelser uafhængigt af hinanden.
    
score = int(input("Indtast din score: "))

if score >= 90:
    print("Du fik en A.")
elif score >= 80:
    print("Du fik en B.")
elif score >= 70:
    print("Du fik en C.")
else:
    print("Du fik en D eller lavere.")
    
#Her vil programmet evaluere scoren og udskrive den tilsvarende karakter baseret på forskellige intervaller.