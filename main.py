# 🚨 Don't change the code below 👇
age = input("What is your current age? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_cap = 90
years_left = age_cap - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
