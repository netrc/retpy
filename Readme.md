

# retpy - retirement planning

You can make a spreadsheet with rows for years and columns for income, expenses, etc. This is fine, but the calculations behind the spreadsheet are hard to see. It's also hard to see why changes in values happen or what sums up to where

This tool uses a programmatic listing of items (income, expenses) and automatic summation to Income, Expense, NetWorth.

Includes settable investment returns, inflation for expenses.

# Functionality

Items
* income - add once/multiple. Does not sum internally - sums to Income col
* investment - add once/multiple; sums internally plus APR mode
* expense - add once/multiple. 

Events
* add an item event once, once every year y1-y2, or every year until end

Runs
* Run events from years y1-y2, or from y1 until death


## Architecture
Essentially building a hard-coded set of spreadsheet cells
* Some built-in columns - net worth, cash, income, expenses
* "columns" are an instance of Income, Expense (others?)
* "rows" are year by year
* hard-coded value fill procedures (addIncome, takeExpense)
* hard-coded transactions (i.e. cell equations), like takeExpenseInflation or transfer
** these are restricted set of cell dependencies
* and restricted/pre-defined outputs - summary columns...

## See Also
* jupyter notebooks
* Stencila - https://stenci.la/