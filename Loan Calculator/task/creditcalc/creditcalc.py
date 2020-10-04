import math
print("Enter the loan principal: ")
principal = float(input())

print("""What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment""")
calculate = input()

if calculate == "m":
    payment = float(input("Enter the monthly payment: "))
    if principal % payment == 0:
        months = principal / payment
        if months == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {months} months to repay the loan")
    else:
        months = principal / payment
        if months - int(math.ceil(months)) < .5:
            months = int(math.ceil(months))
            print(f"It will take {months} months to repay the loan")
        else:
            months = int(math.ceil(months))
            print("It will take {months} months to repay the loan")
elif calculate == "p":
    months = int(input("Enter the number of months: "))
    if principal % months == 0:
        payment = principal / months
        print(f"Your monthly payment = {payment}")
    else:
        payment = principal / months
        if payment - int(math.ceil(payment)) > .5:
            payment = int(math.ceil(payment))
            last_payment = principal - (months - 1) * payment
            print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
        else:
            payment = int(math.ceil(payment))
            last_payment = int(principal - (months - 1) * payment)
            print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
