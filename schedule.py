import random

#Lists
hobbies = ['drawing', 'lettering', 'reading', 'riding', 'video games', 'write']
pt = ['bike','climb','hike','walk','stretch']
academic = ['guitar','spanish','swedish','audiobook','coding','math','philosophy']
wellness = ['journal','meditate','shower','yoga']
options = ['hobbies','pt','academic','wellness']
lettering = ['greek','cursive']
yoga = ['butterfly','lying hip rotation','pigeon','happy baby','cobra','crow','crocodile','downward dog',
        'side angle', 'fire log', 'fish', 'gate','half frog','half pigeon','half lotus','head to knee',
        'lotus','mountain','thunderbolt','tree','triangle',]
result = []

#Makes a random choice from the input list
def rchoice(inputs):
    return(random.choice(inputs))

#Routes choice to a specific category
def catselector(string):
    if (string == 'H'):
        return(rchoice(hobbies))
    elif (string == 'P'):
        return(rchoice(pt))
    elif (string == 'A'):
        return(rchoice(academic))
    elif (string == 'W'):
        return(rchoice(wellness))
    elif (string == 'all' or 'R' or 'no'):
        opt = (rchoice(options))
        catselector(opt)
    else:
        print("Did you choose a valid option?")

#Routes choice to a specific menu option
def menuselector(choice):
    if (choice == 'A'):
        add()
    elif (choice == 'Q'):
        category, amount = input("Please enter the category and amount to add\n").split()
        category = category.upper()
        amount = int(amount)
        mchoice(category, amount)
    elif (choice == 'P'):
        print(result)
    elif (choice == 'C'):
        createday()
    elif (choice == 'R'):
        restart()

#Checks to see if the generated choice is already in the list
def checker(temp, choice):
    while (temp in result) is True:
        temp = catselector(choice)
    if temp not in result:
        return(temp)

#Makes n selections from c category and appends it to the list
def mchoice(choice, number):
    for numbers in range(number):
        number = number - 1
        temp = catselector(choice)
        result.append(checker(temp, choice))

#Print option
def breaker():
    choice = (input("[P]rint list or [C]ontinue?")).upper()
    if choice == "P":
        print(result)

#Takes numbers as input and makes additions to the list
def createday():
    hnum = int(input("How many hobbies would you like to add?\n"))
    mchoice('H', hnum)
    pnum = int(input("How many PT activities would you like to add?\n"))
    mchoice('P', pnum)
    anum = int(input("How many academic activities would you like to add?\n"))
    mchoice('A', anum)
    wnum = int(input("How many wellness activities would you like to add?\n"))
    mchoice('W', wnum)

#Ask for user input and calls mchoice with [choice, number]
def add():
    choice = (input("[H]obbies, [P]t, [A]cademics, [W]ellness\n")).upper()
    number = int(input("#?"))
    mchoice(choice, number)
'''
#
def quickadd(category, amount):
    mchoice(category, amount)'''

#Clears the list
def restart():
    global result
    result = []
    return(result)

#Starts the program
def start():
    print("Options: [C]reate day, [A]dd, [Q]uickadd, [P]rint, [R]estart") #, [E]xit")
    choice = (input()).upper()
    menuselector(choice)

while True:
    start()

'''
Allow the user to go through all their choices, then print the list when finished
'''
