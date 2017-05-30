
from Ret import *

class Scenario:
    def __init__(self,f=None):
        self.cols = {}    # dict of columns
        self.events = {}  # dict of years: list of events
        self.years = []  # list of years
        self.f = f      
        self.rLists = { }

    def addColVal(self, col, y, val):
        if col not in self.cols:
            self.cols[col] = {}
        self.cols[col][y] = val
        # TODO: autodeduce new years here and add to self.years rather than explicit call in Ret.py:36? 
    def addEvent(self,y,ev):
        if y not in self.events:
            self.events[y] = []
        self.events[y].append(ev)
    def addYear(self,y):
        self.years.append(y)
    def getColYear(self,col,y):
        if col not in self.cols:
            return "getCY: bad col"
        if y not in self.cols[col]:
            return "getCY: bad y"
        return self.cols[col][y]
    def printRaw(self):
        for y in self.years:
            # assert - got to be netw, inc, exp, inv columns
            print("{}: {}".format(y,self.events[y])) 
        # TODO: Scenario - fix hack in sort raw columns by class Income, Exp, Inv
    def ritemLists( self, incList, expList, invList ):
            self.rLists["Inc"] = incList
            self.rLists["Exp"] = expList
            self.rLists["Inv"] = invList
    # TODO: Scenario - html print
    # TODO: Scenario - csv? print
    def printRawCols(self):
        self.f.printFamily()
        print("Scenario Run")
        # title line
        print("Year ",end="")
        print("Ages ",end="")
        print("{:>8s}".format("NetW"),end="")
        for c in ["Cash", "Inc", "Exp", "Inv"]:
            print("{:>8s}".format(c),end="")
            for cr in self.rLists[c] if c in self.rLists else []:   # only [] if/when running Scenario tests
                print("{:>8s}".format(cr.name),end="")
        print("")
            
        for y in self.years:
            print("{:<5d}".format(y),end="")
            print("{:<8s}".format(self.f.ageString(y)),end="")

            v = "${:,.0f}".format(self.cols["NetW"][y]) if y in self.cols["NetW"] else ""
            print("{:>8s}".format(v),end="")
            for c in ["Cash", "Inc", "Exp", "Inv"]:
                v = "${:,.0f}".format(self.cols[c][y]) if c in self.cols and y in self.cols[c] else ""
                print("{:>8s}".format(v),end="")
                if c in self.rLists:      # only false if/when running Scenario tests
                    for cr in self.rLists[c]:
                        v = "${:,.0f}".format(self.cols[cr.name][y]) if y in self.cols[cr.name] else ""
                        print("{:>8s}".format(v),end="")
            print("")




if __name__ == '__main__':
    import unittest
    from Family import *
    class TC1(unittest.TestCase):
        def setUp(self):
            self.f = Family("Smith")
            self.f.addPerson( Person("john","john",1970,65,85) )
        def test_feature_one(self):
            s = Scenario(self.f)
            s.addYear(2017)
            s.addEvent(2017,{'e':"someting"})
        def test_feature_two(self):
            s = Scenario(self.f)
            s.addYear(2017)
            s.addEvent(2017,{'e':"someting"})
        def test_print(self):
            s = Scenario(self.f)
            s.addColVal("NetW", 2017, 0.00)
        def test_printRawCols(self):
            s = Scenario(self.f)
            s.addYear(2016)
            s.addColVal("NetW", 2016, 1.00)
            s.addYear(2017)
            s.addColVal("NetW", 2017, 3.00)
            s.addColVal("Inc", 2017, 3.00)
            s.addColVal("Exp", 2017, -2.00)
            s.addYear(2018)
            s.addColVal("NetW", 2018, 4003.00)
            s.addColVal("Inc", 2018, 4000.00)
            s.printRawCols()

    unittest.main()

