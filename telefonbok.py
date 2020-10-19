#Klass som hanterar personer, lagrar namn samt telefonnummer
class Person:

    def __init__(self, n, pN):
        self.name = n
        self.phoneNumber = pN   

#Funktion för prompten
def prompt():
    #Initiera lista för alla personer
    personObject = []
    commandHelp = "Please enter a command.\n List of commands:\n 1. add 'name' 'phone number' \n 2. lookup 'name' \n 3. save 'file name' \n 4. load 'file name' \n 5. alias 'name' 'new name'\n 6. change 'name' 'new number' \n 7. quit"

    #Medan true kör detta
    while True:
        #Lista för input i prompten
        startValues = input('telebok> ').split()


        try:
            #Om Första värdet i listan för inputs är add
            if startValues[0] == 'add':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 3 or len(startValues) < 3:
                    print('Add first name, last name and phone number. No spaces in the phone number')
                    print('Format: (add) (name) (phone number), no paretheses')
                #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    addToPhoneBook(startValues[2], startValues[1], personObject) 
            #Om Första värdet i listan för inputs är lookup
            elif startValues[0] == 'lookup':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 2 or len(startValues) < 2:
                    print('Lookup error:')
                    print('Format: (lookup) (name), no paretheses')
                    #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    lookUp(startValues[1], personObject)
            #Om Första värdet i listan för inputs är save
            elif startValues[0] == 'save':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 2 or len(startValues) < 2:
                    print('Save error:')
                    print('Format: (save) (file name), no paretheses')
                    #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    save(personObject, startValues[1])
            #Om Första värdet i listan för inputs är load
            elif startValues[0] == 'load':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 2 or len(startValues) < 2:
                    print('Load error:')
                    print('Format: (load) (file name), no paretheses')
                    #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    load(personObject, startValues[1])
            #Om Första värdet i listan för inputs är alias
            elif startValues[0] == 'alias':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 3 or len(startValues) < 3:
                    print('Alias error:')
                    print('Format: (alias) (name) (alias), no paretheses')
                    #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    addAlias(startValues[1], startValues[2], personObject)
            #Om Första värdet i listan för inputs är change
            elif startValues[0] == 'change':
                #Om längden på listan för inputs har fel värde så har användaren angett fel antal inputs
                if len(startValues) > 3 or len(startValues) < 3:
                    print('Change error:')
                    print('Format: (change) (name) (new number), no paretheses')
                    #Om längden på listan för inputs har rätt antal inputs så körs funktionen
                else:
                    changeNumber(startValues[1], startValues[2], personObject)
            #Om Första värdet i listan för inputs är quit
            elif startValues[0] == 'quit':
                #break förstör "While True-loopen och stoppar därför koden"
                break
            #Om inget anges så får man upp en lista på kommandon
            else:
                print(commandHelp)

        except IndexError:
            print(commandHelp)

#Funktion som returnerar alla nummer som finns i listan
def checkNumbers(personList):
    numbers = []

    for e in personList:
        numbers.append(e.phoneNumber)

    return(numbers)

#Funktion som returnerar alla namn som finns i listan
def checkNames(personList):
    names = []

    for i in range(0, len(personList)):
        for j in range (0, len(personList[i].name)):
            names.append(personList[i].name[j])

    return(names)
        
#Funktion som lägger till personer i telefonboken
def addToPhoneBook(pNumber, alias, personList):
    try:
        if pNumber in checkNumbers(personList):
            print('This number already exists in the phone book.')
        elif alias in checkNames(personList):
            print('This name already exists in the phone book.')
        else:
            #Gör nytt objekt person med en lista för namn(då alias kan läggas till) samt en sträng för telefonnumret
            newPerson = Person([alias], pNumber)
            #Lägg till personobjektet till listan för personer
            personList.append(newPerson)
            print(alias, 'was added to the phone book.')
        
    except ValueError:
        print('Add first name, last name and phone number. No spaces in the phone number')
        print('(add) (name) (phone number), no paretheses')

#Funktion för att söka på person i telefonboken
def lookUp(searchText, personList):
    found = False
    foundName = ""
    foundNumber = ""
    #Går igenom varje objekt i personlistan
    for e in personList:
        #Om söktexten finns i listan för personnamn(som även inkluderar alla alias för en person)
        if searchText in e.name:
            found = True
            foundName = e.name[0]
            foundNumber = e.phoneNumber
    if found:
        print(searchText + "'s phone number:", foundNumber)
    else:
        print('This person does not exist in the phone book')

#Funktion för att lägga till alias till en person
def addAlias(name, alias, personList):
    addAlias = False
    foundName = ''
    personIndex = 0
    errorMsg = ''
    #Annan variant på forloopen på rad 129
    for i in range(0, len(personList)):
        if name in personList[i].name:
            personIndex = i
            addAlias = True
            continue
        else:
            errorMsg = 'That name does not exist in the phone book'
    
    if alias in checkNames(personList):
        errorMsg = 'The alias you entered already exists in the phone book'
        addAlias = False
    
    if addAlias:
        personList[personIndex].name.append(alias)
        foundName = personList[personIndex].name[0]
        print('Alias', alias, 'was added to', foundName)
    else:
        print(errorMsg)
        
#Funtkion för att ändra nummer
def changeNumber(name, newNumber, personList):
    changeNumber = False
    foundName = ''
    personIndex = 0
    errorMsg = ''
    for i in range(0, len(personList)):
        if name in personList[i].name:
            changeNumber = True
            foundName = personList[i].name[0]
            personIndex = i
            continue
        else:
            errorMsg = 'No person with that name exists in the phone book.'
    
    if newNumber in checkNumbers(personList):
        errorMsg = 'This number already exists in the phone book.'
        changeNumber = False
    
    if changeNumber:
        #I listan med index från den hittade personen, ändra telefonnummer
        personList[personIndex].phoneNumber = newNumber
        print(foundName + "'s number was changed to", newNumber)
    else:
        print(errorMsg)

#Funktion för att spara en telefonbok i en textfil
def save(personList, filename):
    try:
        #Sträng för det som ska läggas till i textfilen
        personAdd = ''
        for p in personList:
            #Lägg till allt från telefonboken i strängen personAdd
            personAdd += p.phoneNumber + ';' + p.name[0] + ';\n'
        phoneBook = open(filename+'.txt', "w")
        #Skriv in strängen personAdd i textfilen
        phoneBook.write(personAdd)
        phoneBook.close()
    except IOError:
       print('The file could not be saved with that name.')

#Funktion för att ladda in en textfil i telefonboken
def load(personList, filename):
    try:
        #Rensa telefonboken för att få in en ren telefonbok utan redundant data
        personList.clear()

        phoneBook = open(filename+'.txt', 'r')

        #Gå igenom alla rader i textfilen
        for line in phoneBook:
            if line == '\n':
                break

            #Gör en lista som innehåller alla namn samt nummer men ta bort alla ';'
            x = line.split(';')
            
            #Lägg till nya personobjekt till listan där x[0] är telefonnumret och x[1] är namnet
            personList.append(Person([x[1]], x[0]))

    except IOError:
        print('That file does not exist.')

prompt()





    

    


