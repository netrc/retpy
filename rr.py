#!/usr/bin/env python

import os
import sys
import logging
from optparse import OptionParser
import fileinput


# comment / strict (?) ordering of items
#Family: "Smith"
#  Person: "John","j",1970,65,85   # name, nickname, birth, ret age, death age

#### Functions for this module/main
def setLog(l):
  logging.basicConfig(level=l)

def someFunc():
  logging.debug("someFunc")
  
#### A Class
class PClass(object):
  def __init__(self, x):
    self.x = x

  def __str__(self):
    return "PClass(" + str(self.x) + ")"

  def value(self):
    return self.x

# A helper to make output easier to see
RPRINT=print

def do_Null(tokens):
  pass
def do_Family(tokens):
  logging.debug("do_Family {}".format(tokens))
  RPRINT("F = Family('{}')".format(tokens[1]))
  
def do_Person(tokens):
  logging.debug("do_Person {}".format(tokens))
  del(tokens[0])
  RPRINT("F.addPerson(Person({})".format(','.join(tokens)))
  #F.addPerson(Person("John","j",1970,65,85))

doToken = {
  "Portfolio:": do_Null,
  "Family:": do_Family,
  "Person:": do_Person
}

#### Main
def main(flist):
  logging.debug("main")
  #p = PClass(9)
  #print(p)

  RPRINT("import sys")
  RPRINT("sys.path.append('lib')")
  RPRINT("from Ret import *")
  RPRINT("#######################")
  # to read stdin or all files on argv
  for line in fileinput.input(flist):
    #logging.debug(">{}".format(line))
    tokens = (' '.join(line.split())).split()   # trim all whitespace, tokenize
    if "#" in tokens:
      tokens = tokens[0:tokens.index("#")]      # remove comments in rest of string
    if len(tokens) == 0: continue   # empty lines  (perhaps line was whole comment)
    logging.debug("real >{}".format(line))

    logging.debug("tokens >{}".format(tokens))
    if tokens[0] not in doToken:
      print("Error: unknown statement>{}< (line:>{}<)".format(tokens[0],line))
      sys.exit(1)

    logging.debug("do token {}".format(tokens[0]))
    f=doToken[tokens[0]]
    f(tokens)
    


if __name__ == '__main__':
  # just supports stdin, and set of option letters 
  pname = sys.argv[0]

  op = OptionParser(usage="%prog [-d] [-t]", version="%prog 0.5")
  op.add_option("-d", "--debug", dest="debugFlag", action="store_true", default=False)
  op.add_option("-t", "--test", dest="doTest", action="store_true", default=False)
  (options, args) = op.parse_args()
  
  runFunc = main  
  if (options.debugFlag):
    setLog(logging.DEBUG)
  if (options.doTest):
    runFunc = unittest.main
    del sys.argv[1:]
    # other args will be parsed by unittest.main

  # or if (len(sys.argv)==3):
  #  	fname=sys.argv[2]

  logging.debug("starting: {}  rest of args:{}".format(pname, sys.argv) )
  runFunc(["r1.r"])
  sys.exit(0)
