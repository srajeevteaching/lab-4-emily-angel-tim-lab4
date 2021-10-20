# Emily Catanzariti, Angel Scott, and Tim Hunt
# Course CS151, Dr. Rajeev
# 10/7/2021
# Lab 4
# Program Inputs: package user has, how many gb used, and whether green package user has coupon
# Program Outputs: cost of phone bill


# define phone bill function
def phone_bill(base_cost, gb_over, base_gb, gb):
    if gb <= base_gb:
        return base_cost
    elif gb > base_gb:
        return base_cost +((gb - base_gb) * gb_over)


# ask user for package
print("The purpose of this program is to calculate your total phone bill based on what package you have.")
package = input("What package do you have?")
package = package.strip().lower()

# assign package to base cost and price for extra gb
if package == "purple":
    base_cost = 99.99
    gb_over = 0
    base_gb = 0
elif package == "orange":
    base_cost = 69.99
    gb_over = 9.99
    base_gb = 4
elif package == "green":
    base_cost = 49.99
    gb_over = 14.99
    base_gb = 2
else:
    print("Sorry your input is invalid.")

# ask user for gb usage to identify any extra costs if applicable
if package == "green" or package == "orange":
    gb = round(float((input("How many GB did you use this month?"))))
    if gb < 0:
        print("Sorry your input is invalid.")

# calculate total cost
if package == "green" or package == "orange":
    total_cost = phone_bill(base_cost, gb_over, base_gb, gb)
elif package == "purple":
    total_cost = base_cost

# ask user if they have coupon, and deduct from total cost if applicable
if package == "green" and gb >= 0:
    coupon = input("Do you have a coupon, yes or no?")
    coupon = str(coupon.strip().lower())
    if coupon == "yes":
        if total_cost >= 75:
            total_cost = total_cost - 20

# output total cost of phone bill
if (package == "green" or package == "orange" and gb >= 0) or package == "purple":
    print("The total cost of your bill is $%.2f" % total_cost)
