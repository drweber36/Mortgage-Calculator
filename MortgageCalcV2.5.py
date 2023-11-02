                ### Mortage Calculator V2.0 ###

### Things To Add: HOA, Payoff Date, Total and Yealy Tax paid, Sales Tax, add error messages


payment_term = 0
down_payment = 0
annual_rate = 0
home_price = 0
monthly_hoa = 0
annual_property_tax = -1

    
# add error messages to each input line
print()
print("Your inputs:")
print()
while home_price < 1 or home_price > 3000000:
  home_price = int(input("Enter the actual price of the home in $: "))
while annual_rate < 0.15 or annual_rate > 99:
  annual_rate = float(input("Enter your APR in %: "))
while payment_term < 1 or payment_term > 31:
  payment_term = int(input("Enter the payment term in years: "))
while down_payment < 1 or down_payment > 2000000:
  down_payment = int(input("Enter your down payment amount in $: "))
while annual_property_tax < 0:
  annual_property_tax = int(input("Enter the estimated annual property tax in $: "))


#Define variables used in mortgage calculator. 
total_property_tax = annual_property_tax * payment_term
monthly_property_tax = annual_property_tax / 12
term_in_months = payment_term * 12
monthly_interest_rate = annual_rate / 1200
finance_amount = home_price - down_payment 
monthly_payment = finance_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -term_in_months) + monthly_property_tax


print()
print()
print("Mortgage Repayment Summary")
print()
print("Your monthly payment is: ${0:,.2f}".format(monthly_payment))
print()
print("Month\t\tRemaining Balance")
print()


#Define running totals 
total_interest_paid = 0
total_monthly_payment = 0
num_months = 0

#While loop to control entire calculations.
remaining_amount = finance_amount


while remaining_amount >= 0:
    num_months += 1
    monthly_interest_payment = monthly_interest_rate * remaining_amount 
    paid_against_principal = monthly_payment - monthly_interest_payment - monthly_property_tax
    remaining_amount -= paid_against_principal

    if remaining_amount < 0:
        print("Month", num_months, "\t\t$0.00")
    else:
        print("Month", num_months, "\t\t${0:,.2f}".format(remaining_amount))
                        
    total_interest_paid += monthly_interest_payment 
    total_mortgage = total_interest_paid + finance_amount + total_property_tax
    total_property_tax_paid = total_property_tax


# Final Print Statements
print()
print("The total cost of this mortgage would be: \n${0:,.2f}".format(total_mortgage))
print()
print("The total interest to be paid on this loan is: \n${0:,.2f}".format(total_interest_paid))
print()
print("The total amount paid for property taxes over the course of the loan is: \n${0:,.2f}".format(total_property_tax_paid))
print()






























