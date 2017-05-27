
import sys
sys.path.append("lib")
from Ret import *
# should be just import R.... R.Port, R.Ritem...

F = Family("Smith")
F.addPerson(Person("John","j",1970,65,85))

#portfolio cash=175 inv=400
P = Portfolio(F,cash=175)

#scenarioA
#income joeIncome 2016 2022 200
joeI = Ritem_income(P,'joeIncome')
joeI.addEvents(2016,2022, lambda r: (r.addIncome('comp1',200)))
joeI.addEventsTilEnd(2023,lambda r: (r.addIncome('ssi',30)))

# some inv fund
invA = Ritem_inv(P,'invA')
invA.addEvent(2015, lambda r: (r.setValue('invA',30)))
invA.addEvents(2015,2027, lambda r: (r.addAPR('invAapr',1.06)))

# ret fund - Joe adds to 401k while working
inv401k = Ritem_inv(P,'inv401k')
inv401k.addEvent(2015, lambda r: (r.setValue('401k.init',10)))
inv401k.addEvents(2016, 2022, lambda r: (r.addValue('401k.contrib',10)))
inv401k.addEvents(2015,2022, lambda r: (r.addAPR('invAapr',1.06)))

# and transfers some to invA while working
joeI.addEvents(2016,2022, lambda r: (r.transfer('trans',invA,25)) )

# add expense in first year $ ; auto inflated
#f-expense house 2014 2023 50
h = Ritem_expense(P,'house')
h.addEvents(2014,2023, lambda r: (r.takeExpense('bigH',50)))
#f-expense house 2024 2027 50
h.addEvents(2024,2027, lambda r: (r.takeExpense('smallH',30)))

trips = Ritem_expense(P,'trips')
trips.addEvent(2025, lambda r: (r.takeExpense('trip',5)))

# inflation for expenses

P.runTilEnd(2014)
P.S.printRawCols()
