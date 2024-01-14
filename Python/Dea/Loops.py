# Loops / Løkker

"""
Et loop er en kontrolstruktur i programmering, der tillader gentagne udførelser af en blok kode.
Dette gør det muligt at automatisere gentagne opgaver og forenkle koden. Der er to hovedtyper af loops i Python: for og while.

For-loopet bruges, når du kender antallet af iterationer på forhånd.

Gør noget med hvert element i listen
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

# Printer tallene 1 til 10

for i in range(5):
    print(i)

#Dette vil udskrive talene 0 til 4, fordi range(5) genererer en sekvens af tal fra 0 til 4.

# Gør noget med hvert element i listen, hvis det er et lige tal

for number in numbers:
  if number % 2==0:
    print(f'{number} er et lige tal')

#While-loopet bruges, når du ikke kender antallet af iterationer på forhånd, og koden skal gentages, så længe en betingelse er sand.
count = 0
while count < 5:
    print(count)
    count += 1    

#Dette vil udskrive talene 0 til 4, fordi blokken gentages, så længe count er mindre end 5.

#Loops giver programmermere fleksibilitet og mulighed for at arbejde med data i gentagne mønstre.
#Det er vigtigt at undgå uendelige loops ved at sikre, at den betingelse, der styrer løkken, vil blive falsk på et tidspunkt.

# Uendeligt loop

#while True:
   #print("Hello World")

# output er "Hello World" i uendelighed

