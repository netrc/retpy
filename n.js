
class Person {
    constructor(name,nick,birthYear,retAge=65,lifeExp=85) {
        this.name = name
        this.nick = nick
        this.birthYear = birthYear
        this.retAge = retAge
        this.lifeExp = lifeExp
    }
    lastYear() {
        return this.birthYear + this.lifeExp
    }
    retYear() {
        return this.birthYear + this.retAge
    }
    summaryString() {
        return `${this.name} (${this.nick}): born ${this.birthYear}, retire at ${this.retAge}, live through ${this.lifeExp}`
    }
}

let x = new Person("Joseph","joe",1961,68,84)
let y = new Person("Mary","mare",1963)


class Family {
  constructor(name) {
    this.name = name
    this.members = []
  }
  addPerson(p) {
    this.members.push(p)
  }
  summaryString() {
    return `${this.name} family`
  }
  lastYear() {
    //python: return Math.max( [ for (p of this.members) p.lastYear() ] )
    // someday... Math.max(...z)
    return Math.max.apply(null, this.members.map( i => i.lastYear() ) )
  }
  printFamily() {
    let s = `# ${this.name} Family\n`
    this.members.forEach( p => s += `#   ${p.summaryString()}\n` )
    s += `## LastYear: ${this.lastYear()}\n`
    console.log(s)
  }
  ageString(y) {
    //return ",".join( [str((y-p.birthYear)) for p in self.members] )
    return `--age--`  
  }
}

let f = new Family("Smith")
f.addPerson(x)
f.addPerson(y)
f.printFamily()


//if __name__ == '__main__':
 // import unittest
  //class TC1(unittest.TestCase):
   // def test_feature_one(self):
    //  print("TC1 test")
     // F = Family("Smith")
      //F.addPerson(Person("Joseph", "joe", 1961))
      //F.addPerson(Person("Mary", "mare", 1966))
      //self.assertEqual(F.summaryString(),"Smith family")
      //self.assertEqual(F.lastYear(), 2051)

  //unittest.main()


//if __name__ == '__main__':
    //import unittest
    //class TC1(unittest.TestCase):
        //def test_feature_one(self):
            //print("TC1 test")
           //P = Person("Joseph", "joe", 1961)
           //self.assertEqual(P.name, "Joseph")
           //self.assertEqual(P.birthYear, 1961)
           //self.assertEqual(P.lastYear(), 2046)
           //self.assertEqual(P.retYear(), 2029)
           //P.retAge = 72
           //self.assertEqual(P.retYear(), 2033)
           //self.assertEqual(P.summaryString(), "Joseph (joe): born 1961, retire at 72, live through 85")//
   //unittest.main()


// # Another type of column; this is mostly a collection of similar typed columns, _income, _expense, etc
class RSummary {
    constructor(name) {      // "Inc", "Exp", "Inv"...
        this.name = name
        this.ritems = []      // list of Ritems per Summary
        RSummary._sumItems[name] = this    // list of all Summary items
                                   // no need to check for existence; should (!) be unique
    }
    static addRitem(name,r) {    // a class method (no self!)
        RSummary._sumItems[name].ritems.push(r)
    }
    static value(name) {    // a class method (no self!)
        theseItems = RSummary._sumItems[name].ritems
        return theseItems.reduce( (acc, r) => acc + r.value, 0)
        // py return sum(r.value for r in RSummary._sumItems[name].ritems)
    }
}
// ugly way to set class member vars
RSummary._sumItems = {}    // collect all the RSummary names


class Portfolio {
    constructor( f ) {
        // if f null, error
        this.family = f
        this.cash = 0
        this.ritems = []
        this.S = null // new Scenario(f)
        this.inflation = 1.03

        new RSummary("Inc")
        new RSummary("Exp")
        new RSummary("Inv")
    }
    ritemsAppend(r) {
        this.ritems.push(r)
    }
    cash() {
        return this.cash
    }
    netWorth() {
//         #print("cash:${}  Inc:${}  Inv:${}  Exp:${}".format( self.cash, RSummary.value("Inc") , RSummary.value("Inv") , RSummary.value("Exp") ))
        return  this.cash + RSummary.value("Inc") + RSummary.value("Inv") - RSummary.value("Exp")        
    }
}           // or should just be a global

let P = new Portfolio(f)

// class Portfolio:            # or should just be a global


//     def summaryString(self):
//         return "c= ${} ${} e= ${} i=${:.0f} ==> ${:.0f}".format(self.cash, RSummary.value("Inc"), RSummary.value("Exp"), RSummary.value("Inv"), self.netWorth())        

//     def run(self,startYear,endYear):
//         logging.debug("INIT: {}".format(self.summaryString()))
//         for y in range(startYear, endYear+1):
//             self.S.addYear(y)
//             logging.debug("Starting: {}".format(y))
//             for sname in RSummary._sumItems:
//                 for r in RSummary._sumItems[sname].ritems:
//                     #logging.debug("...doing item: {}".format(r.name))
//                     # each "event" is a value ?? or a transfer and a value??
//                     r.reset()
//                     r.currentYear = y   # used for various Ritems, e.g. expenseInflation
//                     for e in r.events:
//                         if (e.year == y):
//                             #logging.debug ("... run event: {}".format(e.name))
//                             e.func(r)
//                     # after all the events are done
//                     self.S.addColVal(r.name, y,r.value)
//                     #r.sumToSummary()
//                 self.S.addColVal(sname,y,RSummary.value(sname))

//             logging.debug("{}: {}".format(y, self.summaryString()))
//             # TODO: somehow make NetW and Cash columns like RSummary, so no special adding here
//             self.S.addColVal('NetW',y,self.netWorth())
//             self.cash += RSummary.value("Inc") - RSummary.value("Exp");
//             self.S.addColVal('Cash',y,self.cash)
//             # hack
//             self.S.ritemLists( RSummary._sumItems["Inc"].ritems, RSummary._sumItems["Exp"].ritems, RSummary._sumItems["Inv"].ritems )
//     def runTilEnd(self,startYear):
//         self.run(startYear,self.family.lastYear())

// class Event:
//     def __init__(self,year,func):
//         self.year = year
//         self.func = func
//         self.currentYear = 0

// class Ritem():             # think of this as a column in the sp-sheet
//     def __init__(self,portfolio,name):
//         self.name = name
//         self.taxable = True
//         self.status = True  # == active  ? Status = Enum('Status','Active Inacti
//         self.events = []
//         self.value = 0          ## the instance var for each (col) item
//         self.portfolio = portfolio
//         self.portfolio.ritemsAppend(self)
//     def reset(self):
//         self.value = 0;     # e.g. for income and expense, we start at 0
//                             # cause we put this into P.cash

//     # think of events as adding rows/calcs to this column
//     def addEvent(self, year, func):
//         self.events.append( Event(year, func) )
//     def addEvents(self, firstYear, lastYear, func):
//         for y in range(firstYear,lastYear+1):
//             self.addEvent( y, func )
//         # TODO: inactive is not really used here.....
//         self.events.append( Event(lastYear+1, lambda r: r.inactive) )
//     def addEventsTilEnd(self, firstYear, func):
//         self.addEvents(firstYear,self.portfolio.family.lastYear(), func)
//     def active(self):
//         self.status = True
//     def inactive(self):
//         self.status = False
//     def transfer(self,n,r,v):
//         self.value -= v     # e.g. transfer right out of income
//         r.addValue(n,v)
//         logging.debug("transfer {} {} + ${} => ${}".format(self.name,n,v,self.value))


// # This is a column type - used to manage income, adds up to Income pseudo-col
// class Ritem_income(Ritem):
//     def __init__(self,p,name):
//         super().__init__(p,name)          # there's a main ritem list in the superclass
//         RSummary.addRitem("Inc",self)     # and then a collection list in this named summary column
//     def addIncome(self,n,v):
//         self.value += v
//         logging.debug("income {} {} + ${} => ${}".format(self.name,n,v,self.value))
//     def addValue(self,n,v):
//     		self.addIncome(n,v)

// # This is a column type - used to manage expenses, adds up to expense pseudo-col
// class Ritem_expense(Ritem):
//     def __init__(self,p,name):
//         super().__init__(p,name)
//         RSummary.addRitem("Exp",self)     # and then a collection list in this named summary column
//     def takeExpense(self,n,v):
//         #print("expense {} {} before ${}".format(self.name,n,self.value))
//         self.value += v
//         logging.debug("expense {} {} + ${} => ${}".format(self.name,n,v,self.value))
//     def takeExpenseInflation(self,n,v,baseYear):
//         logging.debug("expenseInflation {} {} before ${}".format(self.name,n,self.value))
//         #print("ei: {} {} {} {} {} {}".format(self.name,n,self.value,self.currentYear,baseYear,self.portfolio.inflation))
//         self.value += v * self.portfolio.inflation**(self.currentYear-baseYear)
//       # add in years
//         logging.debug("expense {} {} + ${} => ${}".format(self.name,n,v,self.value))


// # This is a column type - used to manage investments, adds up to Inv pseudo-col
// class Ritem_inv(Ritem):
//     def __init__(self,p,name):
//         super().__init__(p,name)
//         RSummary.addRitem("Inv",self)     # and then a collection list in this named summary column
//     def reset(self):
//         pass            # for investments, don't reset every year; n.b. overrides base class
//     def setValue(self,n,v):
//         self.value = v
//         logging.debug("inv {} {} set ${} => ${}".format(self.name,n,v,self.value))
//     def addValue(self,n,v):
//         self.value += v
//         logging.debug("inv {} {} add ${} => ${}".format(self.name,n,v,self.value))
//     def addAPR(self,n,rate):
//         self.value *= rate
//         logging.debug("inv {} {} apr ${} => ${}".format(self.name,n,rate,self.value))

// import unittest

// class TC1(unittest.TestCase):
//     def test_feature_one(self):
//         #print("TC1 test")
//         F = Family("Smith");
//         F.addPerson(Person("John","j",1970))
//         P = Portfolio(F)
//         joeI = Ritem_income(P,'joeI')
//         joeI.addEvents(2016,2022, lambda r: (r.addIncome('comp1',2))) # 7 years, $14
//         joeI.addEvents(2021,2022, lambda r: (r.addIncome('comp1',4))) # 2 years, $8  // bonus
//         joeI2 = Ritem_income(P,'joeI2')
//         joeI2.addEvents(2017,2019, lambda r: (r.addIncome('comp2',3)))  # 3 years, $9
//         joeE = Ritem_expense(P,'joeE')
//         joeE.addEvents(2020,2021, lambda r: (r.takeExpense('exp1',4)))  # 2 years, $8
//         P.run(2016,2022)    
//         self.assertEqual(P.S.getColYear("Inc",2016),2)
//         self.assertEqual(P.S.getColYear("Inc",2017),5)
//         self.assertEqual(P.S.getColYear("Inc",2022),6)
//         self.assertEqual(P.S.getColYear("Exp",2021),4)
//         self.assertEqual(P.S.getColYear("NetW",2016),2)
//         self.assertEqual(P.S.getColYear("NetW",2020),15)
//         self.assertEqual(P.S.getColYear("NetW",2022),23)
//         #self.assertEqual(P.netWorth(), 31) # $14 + $8 + $9 = $31
//         # TODO: we don't need to check netWorth? note we can check scenario as above
//         #self.assertEqual(P.netWorth(), 37) # $14 + $8 + $9 = $31
//         P.S.printRawCols()

// if __name__ == '__main__':
//     unittest.main()

