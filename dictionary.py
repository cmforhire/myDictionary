'''
A Simple Dictionary App
Author: Calen Mitchell
'''
# difflib is a library to compare text
import os, sys, json
from difflib import SequenceMatcher, get_close_matches

#loads JSON file
myData = json.load(open("data.json"))

# method for defining the word
def translate(word):
    if word in myData:
        return myData[word]

    #in case the user enter a proper noun, such as Paris or Texas
    elif word.title() in myData:
        return myData[word.title()]

    #in the case the word entered is an acronym
    elif word.upper() in myData:
        return myData[word.upper()]

    #finds words closest to the word entered
    elif len(get_close_matches(word, myData.keys())) > 0:
        answer = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(word, myData.keys())[0]).lower())

        if answer == "y":
            return myData[get_close_matches(word, myData.keys())[0]]


        elif answer == "n":
            return "The word does not exist. Double check entry."

        else:
            return "This word does not exist. Double check entry."

    else:
        return "This word does not exist. Double check entry."

while True:
    # allows user to enter a word, stores as all lowercase
    print('')
    print('Enter the number 0 to end the program.')
    myWord = input("Enter word: ").lower()

    #enter the number 0 to end the program
    if myWord == "0":
        break

    output = translate(myWord)
    if type(output) == list:
        for item in output:
            print(item)
        continue
    else:
        print(output)

print('Thank you for using my Dictionary.')
sys.exit()



