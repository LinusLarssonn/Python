import os
import sys
run = True 
ord = ["Flygplan", "Båt", "Bil"]
beskrivning = ["Flygande plåtburk", "Flytande artefakt", "Rullande kub"]

while run:


    print()
    print("Välj vad du vill göra.\n 1. Lägg till ord i listan.\n 2. Kolla upp ord i listan,\n 3. Stäng av programmet")

    x1 = int(input())

    if(x1==1):
        print("Vilket ord vill du lägga till?")
        x = input()
        ord.append(x)
        print("Hur beskriver du det ordet?")
        x = input()
        beskrivning.append(x)


    elif(x1==2):
        print("Vilket ord vill du kolla upp?")
        y = 0
        for x in ord:
            y += 1
            print(y, x)
        x = int(input())
        print(beskrivning[x-1])

    elif(x1==3):
        print("Program avslutas...")
        run = False
    else: 
        print("Ange ett alternativ mellan 1 & 3")
        continue