from tkinter import *

def readBoth():
    maxLenghtOfTopHundrets = 100
    minimumWordLenght = 3
    gameRules = []
    sortedGameRules = []
    amountOfNumbers = []
    allowedWords = []

    topHundretsNumbers = []
    topHundretsWords = []

    countUp = 0
    topAllHundrets = ""
        
    validwords='wordlist.txt'
    lettervalues='letterValues.txt'


    #opens both files to read them
    with open(validwords, "r") as f:
        allWords = f.read().splitlines()


    #makes a list with the gamerules
    with open(lettervalues, "r") as f:
        for line in f:
            gameRules += line.lower().split(":")
                
        for each in gameRules:
            onepart = each.replace("\n", "")
            try:
                onepart = int(onepart)
            except:
                pass
            sortedGameRules.append(onepart)
                
        #makes a dictionnary
        itter = iter(sortedGameRules)
        dictionnaryRule = dict(zip(itter, itter))

        #calculates every letter trought the dictionnary
        #will also skip the words with lenght over the value of minimumWordLenght
    for eachWord in allWords:
        if not len(eachWord) <= minimumWordLenght:   
            currentNumber = 0
            for eachLetter in eachWord:
                currentNumber += dictionnaryRule[eachLetter]
            amountOfNumbers.append(currentNumber)
            allowedWords.append(eachWord)

    #will take the top 100 words in value
    for each in range(maxLenghtOfTopHundrets):
        countUp += 1
        PlaceAndWord = amountOfNumbers.index(max(amountOfNumbers))
        #extra, all numbers and words in these 2 lists
        topHundretsNumbers.append(amountOfNumbers[PlaceAndWord])
        topHundretsWords.append(allowedWords[PlaceAndWord])
        
        topAllHundrets += (str(countUp) + ". " + allowedWords[PlaceAndWord] + "Valueying :" + str(amountOfNumbers[PlaceAndWord]) + " Points\n")
        del amountOfNumbers[PlaceAndWord]
        del allowedWords[PlaceAndWord]

    #shows on window
    show(topAllHundrets)
            

#for a Tkinter window
def show(content):
    window = Tk()

    showWindow = Text(window, height=30)
    showWindow.insert('1.0', content)
    showWindow.grid()
    
    showWindow.configure(state=DISABLED)

    window.title("Leaderboard")
    window.geometry("500x500")
    window.mainloop()

readBoth()
