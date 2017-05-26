
# TODO: set retirement/death in Person
# TODO: use tax rates
# TODO: how to determine start date - earliest setValue?
# TODO: how to determine end date - life expectency?
# TODO: inflation for expenses
# TODO: normalize addValue / addIncome for all Ritems
# TODO: need addEventAnnual == forever

import sys
sys.path.append("lib")
from Ret import *
# should be just import R.... R.Port, R.Ritem...

F = Family("Campbell")
r = Person("Richard","ric",1961,72)
r = Person("Kristen","krit",1966,68)
F.addPerson(r)

from Ret import *
# should be just import R.... R.Port, R.Ritem...

#portfolio cash=175 inv=400
P = Portfolio(F,cash=50)

#scenarioA
#income joeIncome 2016 2022 200
rI = Ritem_income(P,'rI')
# ric born 1961, ret 68 == 2029
rI.addEvents(2017,2029, lambda r: (r.addIncome('comp1',100)))
rI.addEvents(2030,F.lastYear(), lambda r: (r.addIncome('ssi',36)))

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
trips.addEvent(2035, lambda r: (r.takeExpense('trip',10)))
trips.addEvent(2037, lambda r: (r.takeExpense('trip',10)))


P.run(2016,F.lastYear())

