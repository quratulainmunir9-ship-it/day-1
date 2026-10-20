sales=15000
expenses=5400
profit=sales-expenses
print(profit)


#Task 1 of day 1
sales=25000
expenses=8000
profit=sales-expenses
print(profit)

# task 2 of day 2
# Ek customer ne shop se 3 items khareede:
# - Quantity = 4
# - Price per item = Rs. 1,250
# - Discount = 10%
# Tumhara task:
# 1. total_price calculate karo.
# 2. discount_amount calculate karo.
# 3. Discount minus karke final_price calculate karo.
# 4. final_price print karo.


# Boolean task of day 1
stock = 12
minimum_stock = 5
enough_stock=stock>minimum_stock
print(enough_stock)

# Real Data Science mein use: inventory analysis mein 
# hum check karte hain ke product ka stock minimum 
# required level se kam hai ya nahi.

# IFElse task of dAY1
stock=3
minimum_stock=5
if stock<minimum_stock:
    print("Restock needed")
else:
    print("Stock is enough")
     

# Task 5: if-elif-else
# Ab stock ke 3 levels classify karne hain:
# Stock	Message
# 0–4	"Low stock"
# 5–10	"Medium stock"
# 10 se zyada	"High stock"
# Code mein ye value di gayi hai:

stock = 2

if stock<4:
    print("low stock")
elif stock<10:
    print("medium stock")
else:
    print("high stock")

#     Question
# - Temperature 15 se kam ho → "Cold"
# - Temperature 15 se 29 tak ho → "Warm"
# - Temperature 30 ya us se zyada ho → "Hot"
  
temp=29
if temp<15:
    print("cold")
elif temp<=29:
    print("warm")
else:
    print("hot")


# Ek student exam mein pass tab hoga jab:
# - Marks 50 ya us se zyada hon.
# - Attendance 75% ya us se zyada ho.

marks=65
attendance=75
if marks>=50 and attendance>=75:
    print("PASS")
else:
    print("FAIL")


# FOR LOOP
#     Ek list banao:
# sales = [1200, 2500, 1800, 3000]
# Task: for loop use karke har sale ko print karo.

sales = [1200, 2500, 1800, 3000]
for sale in sales:
    print(sale)

#  Ab loop se har sale print nahi karni, 
# balkay total sales calculate karni hain.


sales = [1200, 2500, 1800, 3000]
total=0
for sale in sales:
    total=sale+total 
print(total)


# for loop aur if use karo.
# Sirf woh sales print hon jo 1000 se zyada hain.


sales = [1200, 2500, 800, 3000]
for sale in sales:
    if sale>1000:
        print(sale)


# Next practice — loop + calculation
# Ab isi sales list mein se 1000 se zyada
# sales ka total calculate karo.

sales = [1200, 2500, 800, 3000]
total=0
for sale in sales:
    if sale>1000:
         total= total+ sale
print(total)


# Next task — khud solve karo
# Ab isi list mein se sirf 1000 
# ya us se kam sales ka total calculate karo:


sales = [1200, 2500, 800, 3000,600,50,45]
total=0
for sale in sales:
    if sale<=1000:
         total= total+ sale
print(total)


# Next practice — count variable
# Ab list mein se count karna hai ke kitni 
# sales 1000 se zyada hain.



# Next task — Average sales
# Ab tum total aur count dono concepts use karogi.



sales = [1200, 2500, 800, 3000,600,50,45]
total=0
count=0
for sale in sales:
    if sale>1000:
     total= total+ sale
    count= count+1
average=total/count
print(average)


#Ab max() function use kiye baghair highest sale find karo.
sales = [1200, 2500, 800, 3000,600,50,45]
highest=sales[0]
for sale in sales:
   if sale>highest:
     highest=sale 
     
print(highest)


# isi tarah lowest sale find karo, min() function use kiye baghair.

sales = [1200, 2500, 800, 3000,600,50,45]
lowest=sales[0]
for sale in sales:
   if sale<lowest:
    lowest=sale 
     
print(lowest)


# Ab list mein se 1000 se bari sales mein highest sale find karo.

sales = [1200, 2500, 800, 3000, 600, 50, 45, 1800]
highest=sales[0]
for sale in sales:
        if sale>1000:
          if sale>highest:
            highest=sale
print(highest)

#logic se 1000 se kam sales mein lowest sale find karo, min() use kiye baghair.
sales = [1200, 2500, 800, 3000,600,50,45]
lowest=sales[0]
for sale in sales:
   if sale<1000:
     if sale<lowest:
      lowest=sale 
     
print(lowest)


# Next practice
# Ab code aise likho ke sirf 1000 se kam sales mein lowest sale find ho, 
# aur agar aisi koi sale na ho to "No matching sale" print ho.

sales = [1200, 2500, 800, 3000,600,50,45]
for sale in sales:
   if sale<1000:
    print(sale)
   else:
    print("No matching found")