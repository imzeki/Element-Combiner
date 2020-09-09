from random import choice, randint
from collections import Counter
import string
import os
from time import ctime
import os

def generateHex():
    """
    Generates a hex
    """
    return '#{:02x}{:02x}{:02x}'.format(randint(0, 250), randint(0, 250), randint(0, 250))

elements_available = ['air', 'water', 'earth', 'fire', 'energy']
elements_used_in_order = []
suggestion_number = 1
indx = len(elements_available)+1
deleted = False
os.chdir('.\\info')

print('Hello! Welcome to Element Combiner! In this game, you create different elements(okay not really elements but more of chemicals) by merging two elements togther. You start with air, water, earth, fire, energy. Combine them and see what result you get! You even get to name them! - Ezekiel. Inspired by Elemental 3 from Carykh.')
print('\n')
while True:
    what_to_do = input('What would you like to do? A) Create new element. B) Show most used elements(Make at least one new element) C) Give a random element D) Give a new element idea E) Return last element created \nF) Search Function Through Numbers, example: #34 G) Name elements in global order H) Delete the element through its name. I) Open info of the element through its name.\n\nAnswer in A, B, C and D and so forth \n').lower()
    if what_to_do == 'a':
        print(f"Element #{indx}")
        newelement = ""
        element1 = input('Name of Element 1 to combine? \n')
        if element1.lower() in elements_available:
            element2 = input('Name of Element 2 to combine? \n')
            if element2.lower() in elements_available:
                while newelement.rstrip() == "":
                    newelement = input('Name of new element? \n')
                if newelement.lower() in elements_available:
                    print("This element already exists!")
                else:
                    elements_used_in_order.append(element1.lower())
                    elements_used_in_order.append(element2.lower())
                    elements_available.append(newelement.lower())
                    indx += 1
                    logo = open(f'{string.capwords(newelement.lower())}.html', 'w+')
                    bc = generateHex()
                    logo.write(f"""
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <title>Data about {string.capwords(newelement)}</title>
                        </head>
                        <body style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">
                            <h1 style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">Element {indx-1}</h1>
                            <p style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">Name of element: {string.capwords(newelement)}</p>
                            <p style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">Made from: {string.capwords(element1.lower())} and {string.capwords(element2.lower())}</p>
                            <p style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">Id: {id(string.capwords(newelement.lower()))}</p>
                            <p style="background-color: {bc}; font-family: "Lucida Console", Courier, monspace; color: #FFFFFF">Color Id: {bc}</p>
                        </body>
                    </html>
                    """)
                    logo.close()
                    os.startfile(f'{string.capwords(newelement.lower())}.html')
            else:
                print(f'Element {element2} does not exist yet.')
        else:
            print(f'Element {element1} does not exist yet.')
    elif what_to_do == 'b':
        try:
            if elements_used_in_order != []:
                num = input('How many elements? \n')
                if int(num) > len(elements_available):
                    print("The number given is more than the elements. It will be defualted to 5.")
                    num = 5
                for i in range(int(num)):
                    print(f"Position: {i+1}. Name: {string.capwords(Counter(elements_used_in_order).most_common()[i][0])}. Count: {Counter(elements_used_in_order).most_common()[i][1]}")
            else:
                print("There are no elements used")
        except:
            print('Integer not detected')
    elif what_to_do == 'c':
        print(choice(elements_available))
    elif what_to_do == 'd':
        print(f"Suggestion #{suggestion_number}: {choice(elements_available)} + {choice(elements_available)}")
        suggestion_number += 1
    elif what_to_do == 'e':
        print("Last new element:", string.capwords(elements_available[-1]))
    elif what_to_do == 'f':
        index = input("What is the number of this element? \n#")
        if index.isnumeric():
            index = int(index)
            if (index-1) > len(elements_available):
                print(f"No elements has the index of #{index}")
            else:
                try:
                    print(f"Element with index of #{index}: {string.capwords(elements_available[index-1])}")
                except:
                    print(f"No elements with the index of #{index} yet.")
        else:
            print("Not an integer")
    elif what_to_do == 'g':
        number = input("Number of elements to show? \n")
        if number.isnumeric():
            number = int(number)+1
            for i in range(number):
                try:
                    print(f"Number {i+1}: {string.capwords(elements_available[i])}")
                except:
                    pass
            print('\n')
        else:
            print("That is not an integer")
    elif what_to_do == 'h':
        nameofelement = input("Name of element to delete? \n").lower()
        try:
            for i in range(len(elements_available)):
                if elements_available[i] == nameofelement:
                    del elements_available[i]
                    deleted = True
                else:
                    pass
            if deleted:
                indx -= 1
                print(f"{string.capwords(nameofelement)} is succesfully deleted.")
            else:
                print("That element does not exist")
        except:
            print("That element does not exist.")

    elif what_to_do == 'i':
        try:
            name = input('Name of element? \n')
            try:
                os.startfile(f'{string.capwords(name.lower())}.html')
            except:
                os.startfile(f'./orginal5/{string.capwords(name.lower())}')
        except:
            print(f'No such element as {string.capwords(name.lower())} yet.')
    else:
        print("Unknown")
