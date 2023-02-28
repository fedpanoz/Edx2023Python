balance = float(input('balance: '))
annualInterestRate = float(input('annual interest rate: '))
monthlyPaymentRate = float(input('monthlyPaymentRate'))
monthlyInterest = annualInterestRate / 12
unpaidBalance = 0
for x in range(12):
    unpaidBalance = (balance - (balance * monthlyPaymentRate))
    balance = unpaidBalance + (unpaidBalance * monthlyInterest)
roundedBalance = round(balance, 2)
print("Remaining balance:", roundedBalance)


