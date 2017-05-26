

class Person:
    def __init__(self,name,nick,birthYear,retAge=68,lifeExp=85):
        self.name = name
        self.nick = nick
        self.birthYear = birthYear
        self.retAge = retAge
        self.lifeExp = lifeExp
    def lastYear(self):
        return self.birthYear + self.lifeExp
    def retYear(self):
        return self.birthYear + self.retAge
    def summaryString(self):
        return "{} ({}): born {}, retire at {}, live through {}".format(self.name, self.nick, self.birthYear, self.retAge, self.lifeExp)




if __name__ == '__main__':
    import unittest
    class TC1(unittest.TestCase):
        def test_feature_one(self):
            print("TC1 test")
            P = Person("Joseph", "joe", 1961)
            self.assertEqual(P.name, "Joseph")
            self.assertEqual(P.birthYear, 1961)
            self.assertEqual(P.lastYear(), 2046)
            self.assertEqual(P.retYear(), 2029)
            P.retAge = 72
            self.assertEqual(P.retYear(), 2033)
            self.assertEqual(P.summaryString(), "Joseph (joe): born 1961, retire at 72, live through 85")

    unittest.main()

