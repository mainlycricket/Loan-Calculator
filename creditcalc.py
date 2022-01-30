import argparse
import math

parser = argparse.ArgumentParser(description="Loan Calculator")

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if args.type == 'annuity':

    # Calculating time period to replay loan
    if (args.principal and args.payment and args.interest) \
            and (args.principal >= 0 and args.payment >= 0 and args.interest >= 0):

        loan_principal = args.principal
        monthly_payment = args.payment
        interest = args.interest

        interest /= 1200

        base = interest + 1
        x = monthly_payment / (monthly_payment - interest * loan_principal)

        n = math.ceil(math.log(x, base))

        if n % 12 != 0:

            years = n // 12
            months = n % 12

            if years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")

            else:
                print(f"It will take {months} months to repay this loan!")

        else:
            years = n // 12
            print(f"It will take {years} years to repay this loan!")

        print("Overpayment=", (monthly_payment * n - loan_principal))

    # Calculating monthly payment
    elif (args.principal and args.periods and args.interest) \
            and (args.principal >= 0 and args.periods >= 0 and args.interest >= 0):

        loan_principal = args.principal
        n = args.periods
        interest = args.interest

        interest /= 1200

        monthly_payment = math.ceil(loan_principal * ((interest * ((interest + 1) ** n)) / (((interest + 1) ** n) - 1)))

        print(f"Your monthly payment = {monthly_payment}!")
        print("Overpayment =", (monthly_payment * n - loan_principal))

    # Calculating loan principal
    elif (args.payment and args.periods and args.interest) \
            and (args.payment >= 0 and args.periods >= 0 and args.interest >= 0):

        annuity = args.payment
        n = args.periods
        interest = args.interest

        interest /= 1200

        loan_principal = annuity / ((interest * ((interest + 1) ** n)) / (((interest + 1) ** n) - 1))

        print(f"Your loan principal = {loan_principal}!")

    else:
        print("Incorrect parameters")
    
elif args.type == 'diff':

    if (args.principal and args.periods and args.interest) \
            and (args.principal >= 0 and args.periods >= 0 and args.interest >= 0):

        loan_principal = args.principal
        n = args.periods
        interest = args.interest

        interest /= 1200

        m = 1   # current month
        total_payment = 0

        while m <= n:

            d = math.ceil((loan_principal / n) + (interest * (loan_principal - (loan_principal * (m - 1)) / n)))
            print(f"Month {m}: payment is {d}")
            total_payment += d
            m += 1

        print("\nOverpayment =", (total_payment - loan_principal))

    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")
