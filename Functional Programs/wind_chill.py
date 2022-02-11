import math


# The formula is not valid when t is greater than 50 (t > 50) and
# v is greater than 120 and less than 3 (3 > v < 120)

v = float(input("Input wind speed in kilometers/hour: "))
if((v >= 3) and (v <= 120)):
    print()
    t = float(input("Input air temperature in degrees Celsius: "))
    if((t >= 0) and (t <= 50)):
        print()
        wc = 35.04 + 0.6215*t + (((0.4275*t) - 35.75)*math.pow(v, 0.16))
        print("The wind chill is", int(round(wc, 0)))
    else:
        print("Enter the correct value of 't'")
else:
    print("Enter the correct value of 'v'")