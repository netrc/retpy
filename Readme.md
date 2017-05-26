

= retpy - retirement planning

You can make a spreadsheet with rows for years and columns for income, expenses, etc. This is fine, but the calculations behind the spreadsheet are hard to see. It's also hard to see why changes in values happen or what sums up to where

This tool uses a programmatic listing of items (income, expenses) and automatic summation to Income, Expense, NetWorth.

Includes settable investment returns, inflation for expenses.

= Functionality

Items
* income
* investment
* expense

Events
* add an item event once, once every year y1-y2, or every year until end

Runs
* Run events from years y1-y2, or from y1 until death

== TODO
# TODO: store run data in Scenario
# TODO: Scenario - raw printout
# TODO: Scenario - table print
# TODO: Scenario - html print
# TODO: Scenario - csv? print
# TODO: item - insurance, with payout
# TODO: item ? long term care?
# TODO: event - person dates are events that trigger things?
#   ? death event stops income?  this means more coupling of items and people
# TODO: set retirement/death in Person
# TODO: use tax rates
# TODO: how to determine start date - earliest setValue?
# TODO: how to determine end date - life expectency?
# TODO: inflation for expenses
# TODO: normalize addValue / addIncome for all Ritems


== DONE
# DONE: need addEventAnnual == forever
