ord = {}
ord['Lampa'] = "Lysande föremål"
ord['Flygplan'] = "Flygande plåtpork"
ord['Bil'] = "Rullande plåtpork"

run = True

while run:
    print()
    print("Välj vad du vill göra.\n 1. Lägg till ord i listan.\n 2. Kolla upp ord i listan,\n 3. Stäng av programmet")

    x1 = int(input())

    if(x1==1):
        print("Vilket ord vill du lägga till?")
        x = input()
        print("Hur beskriver du det ordet?")
        x2 = input()
        if x in ord.keys():
            print("Ordet finns redan")
        else: 
             ord[x] = x2

    elif(x1==2):
        print("Vilket ord vill du ha beskrivet?")
        for key, value in ord.items():
            print(key)
        x = input()
        if x in ord:
            print(ord[x])
        else:
            print("Det ordet finns ej")
            continue
        

    elif(x1==3):
        print("Program avslutas...")
        run = False
    else: 
        print("Ange ett alternativ mellan 1 & 3")
        continue