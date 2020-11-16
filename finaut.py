from trans import Transition
class FiniteAutomaton:
    def __init__(self, file_name):
        self._fileName = file_name
        self._states = []
        self._alphabet = []
        self._transitions = []
        self._initial = ""
        self._final = []
    def getStates(self):
        return self._states
    def getAlphabet(self):
        return self._alphabet
    def getTransitions(self):
        return self._transitions
    def getInitial(self):
        return self._initial
    def getFinal(self):
        return self._final
    def _next(self, start, val):
        for trans in self._transitions:
            if trans.getStart() == start and trans.getVal() == val:
                lst = trans.getEnd()
                return lst[0] #assuming it's a DFA
        return None #no transition found
    def fromFile(self):
        f = open(self._fileName, 'r')
        f.readline()
        states = f.readline()
        states = states.replace('\n', ',')
        states = states.split(',')
        self._states = states
        self._states.pop()
    
        
        f.readline()
        alphabet = f.readline()
        alphabet = alphabet.replace('\n', ',')
        alphabet = alphabet.split(',')
        self._alphabet = alphabet
        self._alphabet.pop()
        
        f.readline()
        trans = f.readline()
        trans = trans.replace('\n', ',')
        while 'initial' not in trans:
            trans = trans.split(',')
            trans.pop()
            newTransition = Transition(trans[0], trans[1])
            endList = []
            for i in range(2, len(trans)):
                endList.append(trans[i])
            newTransition.setEnd(endList)
            self._transitions.append(newTransition)
            trans = f.readline()
            trans = trans.replace('\n', ',')
        
        initial = f.readline()
        self._initial = initial[0]
        f.readline()
        final = f.readline()
        final = final.replace('\n', ',')
        final = final.split(',')
        self._final = final
    def checkDFA(self):
        for trans in self._transitions:
            if len(trans.getEnd()) > 1:
                return False
        return True
   
        
    def checkSequence(self, sequence):
        if not self.checkDFA():
            print("Not a DFA")
            return
        current = self._initial
        for char in sequence:
            next = self._next(current, char)
            print(current + " -> " + char + " -> " + str(next))
            current = next
            if not current:
                return False
        return True    #CROSS CHECK FOR ERRORS? DO I NEED TO CHECK IF IN FINAL STATE?
    