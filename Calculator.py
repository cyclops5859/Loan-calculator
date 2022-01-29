#Created by Cyclops!
import time

monthlyPayment = 0
loan = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0

print ("Welcome to Cyclops bank!")
print ("")
time.sleep(1)
print(r"""
    ----------------------------------------------------------------
     _______           _______  _        _______  _______  _______   
    (  ____ \|\     /|(  ____ \( \      (  ___  )(  ____ )(  ____ \  
    | (    \/( \   / )| (    \/| (      | (   ) || (    )|| (    \/  
    | |       \ (_) / | |      | |      | |   | || (____)|| (_____   
    | |        \   /  | |      | |      | |   | ||  _____)(_____  )  
    | |         ) (   | |      | |      | |   | || (            ) |  
    | (____/\   | |   | (____/\| (____/\| (___) || )      /\____) |  
    (_______/   \_/   (_______/(_______/(_______)|/       \_______)

    ----------------------------------------------------------------
                                                                """)
time.sleep(1)

print ("Let's calculate Your loan....")
print ("")
time.sleep(1)

strLoan = input("Enter your loan amount ($): ")
strInterestRate = input("What's the interest rate on the loan amount (%):  ")
strLoanDurationInYears = input("Estimted time for payback of loan (Years): " )


loanDurationInYears = float(strLoanDurationInYears)
loan = float(strLoan)
interestRate = float(strInterestRate)

numberOfPayments = loanDurationInYears*12

monthlyPayment = loan * interestRate * (1+ interestRate) * numberOfPayments \
    / ((1 + interestRate) * numberOfPayments -1)

print("Your monthly payment will be ($/Year) : ", round(monthlyPayment))
