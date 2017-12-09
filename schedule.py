import sys
import random
import pyperclip

#Lists
hobbies = ['drawing', 'lettering', 'reading', 'riding', 'video games',
           'write']
pt = ['bike','climb','hike','walk','stretch']
academic = ['guitar','spanish','swedish','audiobook','coding','math',
            'philosophy','french']
wellness = ['journal','meditate','shower','yoga']
options = ['hobbies','pt','academic','wellness']
lettering = ['greek','cursive']
yoga = ['butterfly','lying hip rotation','pigeon','happy baby','cobra',
        'crow','crocodile','downward dog','side angle','fire log',
        'fish','gate','half frog','half pigeon','half lotus','head to knee',
        'lotus','mountain','thunderbolt','tree','triangle',]
result = []


#Ask for user input and calls m_choice with [choice, number]
def add():
    choice = (input("[H]obbies, [P]t, [A]cademics, [W]ellness\n")).upper()
    cat_printer(choice)
    number = int(input("#?"))
    m_choice(choice, number)

#Print option
def breaker():
    choice = (input("[P]rint list or [C]ontinue?")).upper()
    if choice == "P":
        print(result)

#Routes choice to a specific category
def cat_selector(string):
    if (string == 'H'):
        return(r_choice(hobbies))
    elif (string == 'P'):
        return(r_choice(pt))
    elif (string == 'A'):
        return(r_choice(academic))
    elif (string == 'W'):
        return(r_choice(wellness))
    elif (string == 'all' or 'R' or 'no'):
        opt = (r_choice(options))
        cat_selector(opt)
    else:
        print("Did you choose a valid option?")

#Prints the corresponding activity
def cat_printer(string):
    if (string == 'H'):
        print(hobbies)
    elif (string == 'P'):
        print(pt)
    elif (string == 'A'):
        print(academic)
    elif (string == 'W'):
        print(wellness)

#Checks to see if the generated choice is already in the list
def checker(temp, choice):
    while (temp in result) is True:
        temp = cat_selector(choice)
    if temp not in result:
        return(temp)

#Takes numbers as input and makes additions to the list
def create_day():
    hnum = int(input("How many hobbies would you like to add?\n"))
    m_choice('H', hnum)
    pnum = int(input("How many PT activities would you like to add?\n"))
    m_choice('P', pnum)
    anum = int(input("How many academic activities would you like to add?\n"))
    m_choice('A', anum)
    wnum = int(input("How many wellness activities would you like to add?\n"))
    m_choice('W', wnum)

def generate():
    m_choice('P', 1)
    m_choice('W', 1)
    m_choice('H', 2)
    m_choice('A', 2)
    print(result)

#Makes n selections from c category and appends it to the list
def m_choice(choice, number):
    for numbers in range(number):
        number = number - 1
        temp = cat_selector(choice)
        result.append(checker(temp, choice))

#Routes choice to a specific menu option
def menu_selector(choice):
    if (choice == 'A'):
        add()
    elif (choice == 'C'):
        create_day()
    elif (choice == 'E'):
        sys.exit()
    elif (choice == 'G'):
        generate()
    elif (choice == 'P'):
        print(result)
    elif (choice == 'Q'):
        category, amount = input("Enter the category and amount to add\n").split()
        category = category.upper()
        amount = int(amount)
        m_choice(category, amount)
    elif (choice == 'R'):
        restart()
        
'''
#
def quickadd(category, amount):
    m_choice(category, amount)'''

#Clears the list
def restart():
    global result
    result = []
    return(result)
    
#Makes a random choice from the input list
def r_choice(inputs):
    return(random.choice(inputs))

#Starts the program
def start():
    print("Options: [C]reate day, [A]dd, [Q]uickadd, [P]rint, [R]estart,", \
            "[G]enerate, [E]xit")
    choice = (input()).upper()
    menu_selector(choice)

while True:
    start()

'''

'''
