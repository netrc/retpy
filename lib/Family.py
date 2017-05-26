
from Person import *

class Family:
  def __init__(self,name):
    self.name = name
    self.members = []
  def addPerson(self,p):
    self.members.append(p)
  def summaryString(self):
    return "{} family".format(self.name)
  def lastYear(self):
    return max( [ p.lastYear() for p in self.members ] )
    


if __name__ == '__main__':
  import unittest
  class TC1(unittest.TestCase):
    def test_feature_one(self):
      print("TC1 test")
      F = Family("Smith")
      F.addPerson(Person("Joseph", "joe", 1961))
      F.addPerson(Person("Mary", "mare", 1966))
      self.assertEqual(F.summaryString(),"Smith family")
      self.assertEqual(F.lastYear(), 2051)

  unittest.main()

