principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Rate cant be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time cant be less than or equal to zero")

print(f"Your compound interest is: {round(principle * pow((1 + rate /100), time), 3)}")