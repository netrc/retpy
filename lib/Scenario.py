
class Scenario:
    def __init__(self):
        self.cols = {}    # dict of columns
        self.events = {}  # dict of years: list of events
        self.years = []  # list of years

    def addColVal(self, col, y, val):
        if col not in self.cols:
            self.cols[col] = {}
        self.cols[col][y] = val
    def addEvent(self,y,ev):
        if y not in self.events:
            self.events[y] = []
        self.events[y].append(ev)
    def addYear(self,y):
        self.years.append(y)
    def printRaw(self):
        for y in self.years:
            # assert - got to be netw, inc, exp, inv columns
            print("{}: {}".format(y,self.events[y])) 
    def printRawCols(self):
        print("Scenario Run")
        print("Year ",end="")
        for c in self.cols:
            # title line
            print("{:>8s}".format(c),end="")
        print("")
        for y in self.years:
            print("{:<5d}".format(y),end="")
            for c in self.cols:
                v = "${:,.0f}".format(self.cols[c][y]) if y in self.cols[c] else ""
                print("{:>8s}".format(v),end="")
            print("")




if __name__ == '__main__':
    import unittest
    class TC1(unittest.TestCase):
        def test_feature_one(self):
            s = Scenario()
            s.addYear(2017)
            s.addEvent(2017,{'e':"someting"})
        def test_feature_two(self):
            s = Scenario()
            s.addYear(2017)
            s.addEvent(2017,{'e':"someting"})
        def test_print(self):
            s = Scenario()
            s.addColVal("NetW", 2017, 0.00)
        def test_printRawCols(self):
            s = Scenario()
            s.addYear(2016)
            s.addColVal("NetW", 2016, 1.00)
            s.addYear(2017)
            s.addColVal("NetW", 2017, 3.00)
            s.addColVal("Incm", 2017, 3.00)
            s.addColVal("Exp", 2017, -2.00)
            s.addYear(2018)
            s.addColVal("NetW", 2018, 4003.00)
            s.addColVal("Incm", 2018, 4000.00)
            s.printRawCols()

    unittest.main()
