# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection
# search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt
# within a year
balance = float(input('balance: '))
annualInterestRate = float(input('annual interest rate: '))
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0
originalBalance = balance
low = balance / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12
epsilon = 0.01
while abs(balance) >= epsilon:
    monthlyPayment = (high + low) / 2
    balance = originalBalance
    for month in range(1, 13):
        balance -= monthlyPayment
        balance += balance * monthlyInterestRate
        if balance <= 0:
            break
    if balance > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
print('Lowest Payment:', round(monthlyPayment, 2))


