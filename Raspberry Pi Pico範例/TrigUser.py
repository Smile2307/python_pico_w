import math
angle = float(input("Enter angle in degrees: "))
trig = input("Sine (s), cosine (c), or tangent (t): ")
rad = math.radians(angle)

if trig == "s":
    print(math.sin(rad))
elif trig == "c":
    print(math.cos(rad))
elif trig == "t":
    print(math.tan(rad))
else:
    print("Error in input")