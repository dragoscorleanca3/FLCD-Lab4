class Transition:
    def __init__(self, st = None, va = None, en = None):
        self._start = st
        self._val = va
        self._end = en
        
    def __str__(self):
        string = "δ : " + self._start + " X " + self._val + " --> " + str(self._end)
        return string
    
    def getStart(self):
        return self._start
    def getVal(self):
        return self._val
    def getEnd(self):
        return self._end
    
    def setStart(self, _start):
        self._start = _start
    def setVal(self, _val):
        self._val = _val
    def setEnd(self, _end):
        self._end = _end