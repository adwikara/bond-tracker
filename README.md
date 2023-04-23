# bond-tracker
A tool to keep track of Indonesian bond investments

Here is an example:

Inputs:
```
coupon = 0.0625
bond_price = 100.00
purchase_value = 200000000
d_today = date.today()
d_settlement = date(2021, 8, 16)
d_coupon_last = date(2021, 6, 16)
d_coupon_next = date(2021, 12, 15)
d_end = date(2036, 8, 16)
payments_per_year = 2 #FR = 2, ORI = 12, SR = 12
```

Outputs:
```
-----INPUT PARAMETERS-----
Coupon Rate: 6.25%
Bond Price to Par: 100.0%
Purchase Value: Rp 200,000,000.00
Bond Type: FR


-----ANALYSIS TO MATURITY-----
Purchase Price: Rp 202,089,041.10
Total Investment Value to Maturity: Rp 374,375,000.00
Total Profit to Maturity: Rp 172,285,958.90
Profit Rate to Maturity: 86.14%
Profit Rate per Year: 5.74%


-----ANALYSIS TO DATE-----
Purchase Price: Rp 202,089,041.10
Total Investment Value to Date: Rp 222,500,000.00
Total Profit to Date: Rp 20,410,958.90
Profit Rate to Date: 10.21%
Profit Rate per Year: 5.1%
```
