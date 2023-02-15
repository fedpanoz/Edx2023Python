balance = float(input('balance: '))
annualInterestRate = float(input('annual interest rate: '))

monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0
originalBalance = balance

while balance > 0:
    monthlyPayment += 10
    balance = originalBalance
    lowMonthly = originalBalance / 12
    highMontly = (originalBalance(1 + monthlyInterestRate) ** 12.0)
    midMontly = (lowMonthly + highMontly) / 2

    for month in range(1, 13):
        balance -= monthlyPayment
        balance += balance * monthlyInterestRate
        if balance <= 0:
            break

print('Lowest Payment:', monthlyPayment)
