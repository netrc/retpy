
import logging
from Family import *
from Scenario import *

class Portfolio:            # or should just be a global
    def __init__(self, f, cash=0):
        self.family = f    # ?
        self.cash = cash    # ?
        self.ritems = []
        self.S = Scenario()

    def ritemsAppend(self,r):
        self.ritems.append(r)

    def cash(self):
        return self.cash;

    def netWorth(self):
        return( self.cash + Ritem_income.value() + Ritem_inv.value() - Ritem_expense.value() )

    def summaryString(self):
        return "c= ${} ${} e= ${} i=${:.0f} ==> ${:.0f}".format(self.cash, Ritem_income.value(), Ritem_expense.value(), Ritem_inv.value(), self.netWorth())
        

    def run(self,startYear,endYear):
        logging.debug("INIT: {}".format(self.summaryString()))
        for y in range(startYear, endYear):
            self.S.addYear(y)
            logging.debug("Starting: {}".format(y))
            Ritem_inv.invSumReset()
            Ritem_income.incSumReset()
            Ritem_expense.expSumReset()
            for r in [r for r in self.ritems if r.status]:
                #logging.debug("...doing item: {}".format(r.name))
                # each "event" is a value ?? or a transfer and a value??
                r.reset()
                for e in r.events:
                    if (e.year == y):
                        #logging.debug ("... run event: {}".format(e.name))
                        e.func(r)
                # after all the events are done
                self.S.addColVal(r.name, y,r.value)
                r.sumToSummary()
            logging.debug("{}: {}".format(y, self.summaryString()))
            self.S.addColVal('NetW',y,self.netWorth())
            self.S.addColVal('Inc',y,Ritem_income.value())
            self.S.addColVal('Exp',y,Ritem_expense.value())
            self.S.addColVal('Inv',y,Ritem_inv.value())
            self.cash += Ritem_income.value() - Ritem_expense.value();
    def runTilEnd(self,startYear):
        self.run(startYear,self.family.lastYear())

class Event:
    def __init__(self,year,func):
        self.year = year
        self.func = func

class Ritem():             # think of this as a column in the sp-sheet
    def __init__(self,portfolio,name):
        self.name = name
        self.taxable = True
        self.status = True  # == active  ? Status = Enum('Status','Active Inacti
        self.events = []
        self.value = 0          ## the instance var for each (col) item
        self.portfolio = portfolio
        self.portfolio.ritemsAppend(self)
    def reset(self):
        self.value = 0;     # e.g. for income and expense, we start at 0
                            # cause we put this into P.cash

    # think of events as adding rows/calcs to this column
    def addEvent(self, year, func):
        self.events.append( Event(year, func) )
    def addEvents(self, firstYear, lastYear, func):
        for y in range(firstYear,lastYear+1):
            self.events.append( Event(y, func) )
        self.events.append( Event(lastYear+1, lambda r: r.inactive) )
    def addEventsTilEnd(self, firstYear, func):
        self.addEvents(firstYear,self.portfolio.family.lastYear(), func)
    def active(self):
        self.status = True
    def inactive(self):
        self.status = False
    def transfer(self,n,r,v):
        self.value -= v     # e.g. transfer right out of income
        r.addValue(n,v)
        logging.debug("transfer {} {} + ${} => ${}".format(self.name,n,v,self.value))


# This is a column type - used to manage income, adds up to Income pseudo-col
class Ritem_income(Ritem):
    _incSumValue = 0 # class variable
    def __init__(self,p,name):
        super().__init__(p,name)
    def addIncome(self,n,v):
        self.value += v
        logging.debug("income {} {} + ${} => ${}".format(self.name,n,v,self.value))
    def addValue(self,n,v):
    		self.addIncome(n,v)
    def sumToSummary(self):
        #print("inv sum to summary")
        Ritem_income._incSumValue += self.value
    # class (summary column) methods   # no self
    def incSumReset():
        #print("inv sum reset")
        Ritem_income._incSumValue = 0
    def value():
        return Ritem_income._incSumValue

# This is a column type - used to manage expenses, adds up to expense pseudo-col
class Ritem_expense(Ritem):
    _expSumValue = 0 # class variable
    def __init__(self,p,name):
        super().__init__(p,name)
    def takeExpense(self,n,v):
        #print("expense {} {} before ${}".format(self.name,n,self.value))
        self.value += v
        logging.debug("expense {} {} + ${} => ${}".format(self.name,n,v,self.value))
    def sumToSummary(self):
        Ritem_expense._expSumValue += self.value
        #print("exp sum to sum = {}".format(Ritem_expense._expSumValue))
    # class (summary column) methods   # no self
    def expSumReset():
        Ritem_expense._expSumValue = 0
        #print("exp sum reset = {}".format(Ritem_expense._expSumValue))
    def value():
        return Ritem_expense._expSumValue


# This is a column type - used to manage investments, adds up to Inv pseudo-col
class Ritem_inv(Ritem):
    _invSumValue = 0 # class variable
    def __init__(self,p,name):
        super().__init__(p,name)
    def reset(self):
        pass            # for investments, don't reset every year
    def setValue(self,n,v):
        self.value = v
        logging.debug("inv {} {} set ${} => ${}".format(self.name,n,v,self.value))
    def addValue(self,n,v):
        self.value += v
        logging.debug("inv {} {} add ${} => ${}".format(self.name,n,v,self.value))
    def addAPR(self,n,rate):
        self.value *= rate
        logging.debug("inv {} {} apr ${} => ${}".format(self.name,n,rate,self.value))
    def sumToSummary(self):
        #print("inv sum to summary")
        Ritem_inv._invSumValue += self.value
    # class (summary column) methods   # no self
    def invSumReset():
        #print("inv sum reset")
        Ritem_inv._invSumValue = 0
    def value():
        return Ritem_inv._invSumValue

import unittest

class TC1(unittest.TestCase):
    def test_feature_one(self):
        print("TC1 test")
        F = Family("Smith");
        F.addPerson(Person("John","j",1970))
        P = Portfolio(F)
        joeI = Ritem_income(P,'joeIncome')
        joeI.addEvents(2016,2022, lambda r: (r.addIncome('comp1',2)))
        P.run(2016,2022)    # 7 years, $14
        self.assertEqual(P.netWorth(), 14)

if __name__ == '__main__':
    unittest.main()





