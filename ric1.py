

import sys
sys.path.append("lib")
from Ret import *
# should be just import R.... R.Port, R.Ritem...

F = Family("Campbell")
F.addPerson( Person("Richard","ric",1961,72) )
F.addPerson( Person("Kristen","krit",1966,68) )

from Ret import *
# should be just import R.... R.Port, R.Ritem...

#portfolio cash=175 inv=400
P = Portfolio(F,cash=50)

#scenarioA
#income joeIncome 2016 2022 200
rI = Ritem_income(P,'rI')
# ric born 1961, ret 68 == 2029
rI.addEvents(2017,2029, lambda r: (r.addIncome('r',100)))
rI.addEvents(2030,F.lastYear(), lambda r: (r.addIncome('r-ssi',36)))
# k born 1966, ret 65 == 2031
rI.addEvents(2017,2031, lambda r: (r.addIncome('k',100)))
rI.addEvents(2032,F.lastYear(), lambda r: (r.addIncome('k-ssi',36)))

invA = Ritem_inv(P,'invA')
invA.addEvent(2016, lambda r: (r.setValue('invA',300)))
invA.addEvents(2017,2030, lambda r: (r.addAPR('invAapr',1.06)))

#joeI.addEvents(2016,2022, lambda r: (r.transfer('trans',invA,25)) )
invA.addEvents(2030,F.lastYear(), lambda r: (r.transfer('trans',rI,25)) )

# add expense in first year $ ; auto inflated
#f-expense house 2014 2023 50
h = Ritem_expense(P,'house')
# kids out 2005+18 = 2033
h.addEvents(2017,2033, lambda r: (r.takeExpense('bigH',50)))
#f-expense house 2024 2027 50
h.addEvents(2034,F.lastYear(), lambda r: (r.takeExpense('smallH',30)))

#living expenses
l = Ritem_expense(P,'lE')
l.addEvents(2017,2033, lambda r: (r.takeExpense('living',50)))
l.addEvents(2034,F.lastYear(), lambda r: (r.takeExpense('living',30)))

trips = Ritem_expense(P,'trips')
trips.addEvents(2032,2042, lambda r: (r.takeExpense('trip',10)))


P.run(2016,F.lastYear())
P.S.printRawCols()
