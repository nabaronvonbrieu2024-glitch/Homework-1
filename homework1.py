gross = float(input("enter gross salary: "))

#1. If the gross is less than 1000, then the income tax is 10%
if gross < 1000:
    tax_rate = 0.10
#2. If the gross is less than 2000, then the income tax is 12%
elif gross < 2000:
    tax_rate = 0.12
#3. If the gross is less than 4000, then the income tax is 14%
elif gross < 4000:
    tax_rate = 0.14
#4. If the gross is more than 4000, then the income tax is 18%
else:
    tax_rate = 0.18
#5. If the gross is less than 2000, every child gets you a tax cut of 1%
children = int(input("Enter number of children"))
if gross < 2000:
    cut_per_child = 0.01


#6. If the gross is more than 2000, every child gets you a tax cut of 0.5%
else:
    cut_per_child = 0.005

tax_rate = tax_rate - (children * cut_per_child)

print("Tax rate is ", tax_rate)
print("tax rate after child cut:", tax_rate)
