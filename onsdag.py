import os, random, time #importerar modulerna os, random och time. 

loop = 0 #bestämmer ett värde på variabeln loop med en tilldelninsoperator så att programmet inte kraschar.
svar = 0 #bestämmer ett värde på variabeln svar med en tilldelningsoperator så att programmet inte kraschar.

while loop !=3: #medans värdet på loop inte är 3 så fortsätter loopen tills den får rätt input. (Kan alltså avsluta programmet genom att trycka på 3.)
    try: #försöker...
        loop = int(input("Är det här en häftig loop? JA (1) NEJ (2)")) #ställer användaren en viktig fråga.
    except: #annars...
        print("Du måste besvara frågan med antingen JA (1) eller NEJ (2) för att bryta dig ut ur denna häftiga loop") #skriver den ut detta.
    if loop == 1: #om användaren tryckte på 1...
        svar = random.randint(1,3) #så slumpar programmet fram en siffra som bestämmer vilket svar som kommer att skrivas ut i terminalen.
        if svar == 1: #om svar variabeln fick värdet 1 efter slumpningen så printar den...  
            print("Korrekt svar") #skriver ut ett svar i terminalen.
            break #stoppar.
        elif svar == 2: #om svar variabeln fick värdet 2 efter slumpningen så printar den...
            print("Du har rätt") #skriver ut ett annat svar i terminalen
            break #stoppar.
        elif svar == 3: #om svar variabeln fick värdet 3 efter slumpningen så printar den...
            print("Du är den utvalde") #skriver ut ett hemligt svar i terminalen.
            time.sleep(3) #programmet väntar i 3 sekunder innan det fortsätter köra kvarstående kommandon.
            os.system('cls') #eftersom att jag importerat os tidigare så kan programmet använda ett system kommando för att tömma terminalen så att användaren blir förvirrad.
            time.sleep(3) #programet väntar i ytterligare 3 sekunder till för att överraska användaren med nästa print.
            print("Men du vinner ingenting") #skriver ut ett meddelande i terminalen.
            break #stoppar.
    if loop == 2: #om användaren trycke på 2...
        print("Fel svar") #skriver programmet ut ett meddelande i terminalen. 
                          #eftersom att jag inte satt en break här kommer programmet fortsätta ställa samma fråga tills användaren svarat rätt d.v.s JA (1)
# ()Parenteser 
# :Kolon 
# ;Semikolon 
# /Snedstreck 
# \Omvänt snedstreck
# {}Måsvingar 
# "" Dubbelsnuttar (Jens version av citattecken)
# > Större än
# < Mindre än
# == Lika med
# = Tilldelningsoperator (Likhetstecken)
# ''Apostrofer
# # Fyrkant
# ! Inte lika med (Utropstecken)
# >= Större än eller lika med
# <= Mindre än eller lika med

#Hälsning = "Hej Jens" #ta bort fyrkanten för att test-köra denna kod
#for c in Hälsning: #ta bort fyrkanten för att test-köra denna kod
    #print("one letter " + c) #ta bort fyrkanten för att test-köra denna kod
