from finaut import FiniteAutomaton
def menu():
    print("0. Exit")
    print("1. States")
    print("2. Alphabet")
    print("3. Transitions")
    print("4. Initial state")
    print("5. Final state")
    print("6. DFA True or False")
    print("7. Test ? sequence accepted by FA")
    
menu()
fa = FiniteAutomaton("fa")
fa.fromFile()
inp = int(input("Choice: "))  
while inp:
    if inp == 1:
        print(fa.getStates())
    elif inp == 2:
        print(fa.getAlphabet())
    elif inp == 3:
        for trans in fa.getTransitions():
            print(trans)
    elif inp == 4:
        print(fa.getInitial())
    elif inp == 5:
        print(fa.getFinal())
    elif inp == 6:
        print(fa.checkDFA())
    elif inp == 7:
        someString = input("Enter sequence: ")
        print(fa.checkSequence(someString))

    inp = int(input("Choice: "))

    
    
    