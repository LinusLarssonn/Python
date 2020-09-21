ord = [("Båt", "En flytande manick"), ("Bil", "En rullande kub"),("Flygplan", "En obiologisk fågel")]
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
        ord.append(tuple([x, x2]))

    elif(x1==2):
        y = 0
        print()
        print("Vilket ord vill du ha beskrivet?")
        for y1 in range(0, len(ord)):
            y += 1
            print(y, ord[y1][0])
        x = int(input())
        print(ord[x-1][1])

    elif(x1==3):
        print("Program avslutas...")
        run = False
    else: 
        print("Ange ett alternativ mellan 1 & 3")
        continue