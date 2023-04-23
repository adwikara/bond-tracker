
from datetime import date
import math

# define inputs
coupon = 0.0625
bond_price = 100.00
purchase_value = 200000000
d_today = date.today()
d_settlement = date(2021, 8, 16)
d_coupon_last = date(2021, 6, 16)
d_coupon_next = date(2021, 12, 15)
d_end = date(2036, 8, 16)
payments_per_year = 2 #FR = 2, ORI = 12, SR = 12

# print the input parameters
def print_input_param():
    print("\n")
    print("-----INPUT PARAMETERS-----")
    print("Coupon Rate: "+str(coupon*100)+"%")
    print("Bond Price to Par: "+str(bond_price)+"%")
    print("Purchase Value: "+print_as_idr(purchase_value))
    print("Bond Type: FR")
    print("\n")

# parse currency
def print_as_idr(price):
    #price = 213439.28
    seperator_of_thousand = "."
    seperator_of_fraction = ","
    my_currency = "Rp {:,.2f}".format(price)
    if seperator_of_thousand == ".":
        main_currency, fractional_currency = my_currency.split(".")[0], my_currency.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        currency = new_main_currency + seperator_of_fraction + fractional_currency
    #print(my_currency)
    return str(my_currency)

# get date comparison function, number of days between dates
def get_days(d0,d1):
    delta = d0 - d1
    return delta.days

# calculate acrued interest
def get_accrued_interest(d0,d1):
    days_accrued = get_days(d0, d1)
    total = purchase_value * coupon * (days_accrued/365)
    return total
    
# calculate purchase price
def get_purchase_price():
    accrued_interest = get_accrued_interest(d_settlement,d_coupon_last)
    total = purchase_value * (bond_price/100) + accrued_interest
    print("Purchase Price: "+ print_as_idr(total))
    return total

# calculate interest payment value
def get_interest_value():
    bond_tax = 0.9
    interest = purchase_value * coupon * (1/payments_per_year) * bond_tax
    #print(interest)
    return interest

# profit analysis to maturity
def return_to_maturity():
    print("-----ANALYSIS TO MATURITY-----")
    days_to_maturity = get_days(d_end, d_settlement)
    #print(days_to_maturity)
    number_of_payments = math.ceil(days_to_maturity/(365/payments_per_year))
    #print(number_of_payments)
    total_coupon = get_interest_value()*number_of_payments
    #print(total_coupon)
    total_return_maturity = total_coupon+purchase_value
    total_profit = total_return_maturity - get_purchase_price()
    profit_rate = 100*(total_profit/purchase_value)
    profit_rate_per_year = profit_rate/(d_end.year - d_settlement.year)
    print("Total Investment Value to Maturity: "+print_as_idr(total_return_maturity))
    print("Total Profit to Maturity: "+print_as_idr(total_profit))
    print("Profit Rate to Maturity: "+str(round(profit_rate,2))+"%")
    print("Profit Rate per Year: "+str(round(profit_rate_per_year,2))+"%")
    print("\n")

# profit analysis to date
def return_to_date():
    print("-----ANALYSIS TO DATE-----")
    days_to_date = get_days(d_today, d_settlement)
    number_of_payments = math.ceil(days_to_date/(365/payments_per_year))
    total_coupon = get_interest_value()*number_of_payments
    total_return_to_date = total_coupon+purchase_value
    total_profit = total_return_to_date - get_purchase_price()
    profit_rate = 100*(total_profit/purchase_value)
    print("Total Investment Value to Date: "+print_as_idr(total_return_to_date))
    print("Total Profit to Date: "+print_as_idr(total_profit))
    print("Profit Rate to Date: "+str(round(profit_rate,2))+"%")
    profit_rate_per_year = profit_rate/(d_today.year - d_settlement.year)
    print("Profit Rate per Year: "+str(round(profit_rate_per_year,2))+"%")
    print("\n")

# run program
print_input_param()
return_to_maturity()
return_to_date()