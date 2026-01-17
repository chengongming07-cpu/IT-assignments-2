  #exercise 1: 

zander = float(input("Enter Zander's length in cm: "))
if zander < 42:
        print("Zander is not long enough to keep fishing, centimeters below the size limit the caught fish is need to be longer than 42.")
else: 
        print("Zander is long enough to keep fishing.")

 

#exercise 2: 
try:
    cabin_class = input("Enter cabin class (LUX, A, B, or C): ")
    if cabin_class == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

except ValueError:
    print("Invalid cabin class.")

#exercise 3:
biologocal_sex = input("Enter biological sex (M/F): ")
hemoglobin_value = float(input("Enter hemoglobin value (g/L): "))
if biologocal_sex == "M":
    if hemoglobin_value >= 134 and hemoglobin_value <= 167:
        print("you have normal hemoglobin.")
    elif hemoglobin_value < 134:
        print("your hemoglobin is low.")
    else:
        print("your hemoglobin is high.")
if biologocal_sex == "F":
    if hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print("you have normal hemoglobin.")
    elif hemoglobin_value < 117:
        print("your hemoglobin is low.")
    else:
        print("your hemoglobin is high.")

#exercise 4:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#exercise 5:
import math

def unit_price(diameter_cm, price_usd):
    radius_m = diameter_cm / 2 / 100   # đổi cm -> m
    area = math.pi * radius_m ** 2
    return price_usd / area

print("Enter information for pizza 1:")
d1 = float(input("Diameter (cm): "))
p1 = float(input("Price (USD): "))

print("\nEnter information for pizza 2:")
d2 = float(input("Diameter (cm): "))
p2 = float(input("Price (USD): "))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

print(f"\nPizza 1 unit price: {price1:.2f} USD/m^2")
print(f"Pizza 2 unit price: {price2:.2f} USD/m^2")

if price1 < price2:
    print("Pizza 1 provides better value for money.")
elif price2 < price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value.")






      