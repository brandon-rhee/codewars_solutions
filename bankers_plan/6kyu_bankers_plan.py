
"""
Result Link: https://www.codewars.com/kata/reviews/56445e8a55d0e45b8c000116/groups/676689e8f47a8738eb879af3
Write a function fortune to determine if John can sustain yearly withdrawals from his bank account for a given number of years (n). The account earns interest annually, withdrawals increase due to inflation, and all calculations are truncated to integers. Return True if the account balance never goes negative over the years; otherwise, return False.
step1: deposit(fo) money in year 1
step2: percent(p) per year
step3: withdraw(c0) each year. Take into infation (i) constant

notes: withdraw amount is dynamic based on year due to interest
        deposit amount is dynamic based on year
"""
from decimal import Decimal as D, ROUND_DOWN

def fortune(f0,p,c0, n, i):
    bank_account_list = []
    bank_account = D(f0)
    withdraw_amount = D(c0)
    interest = D(p) / 100
    inflation = D(i) / 100
    for year in range(1,n+1):
        if year == 1:
            bank_account = bank_account
            withdraw_amount = withdraw_amount
        else:
            bank_account = (bank_account + (interest * bank_account) - withdraw_amount).quantize(D('1'), rounding=ROUND_DOWN) # prevents floating point rounding errors
            bank_account_list.append(bank_account)
            withdraw_amount = (withdraw_amount * (1 + inflation)).quantize(D('1'), rounding=ROUND_DOWN)
        if bank_account < 0:
            bank_account_list.append(bank_account)
            break


    enumerate_obj = enumerate(bank_account_list,1)
    enumerated_list = list(enumerate_obj)

    if enumerated_list[-1][1] < 0:
        # print(f"{enumerated_list[-1][1]}, he has no way to withdraw something for his living in year {enumerated_list[-1][0]}")
        return False

    else:
        # print(f"{enumerated_list[-1][1]}, he has money to withdraw something for his living in year {enumerated_list[-1][0]}")
        return True

fortune(100000000, 5, 1000000, 50, 1)
