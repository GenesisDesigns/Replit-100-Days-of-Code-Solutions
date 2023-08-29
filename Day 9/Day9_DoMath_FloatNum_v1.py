#Title: Replit Day  - Day9 - Casting Spells On Your Code - Do math with float numbers - v1

print("Generation Identifier")
yrBorn = int(input("What year were you born: "))
print(yrBorn)
if yrBorn >= 1883 and yrBorn <= 1900:
    print("You are from the 'Lost Generation!'")
elif yrBorn >= 1901 and yrBorn <= 1927:
    print("You are from the 'Greatest Generation!'")
elif yrBorn >= 1928 and yrBorn <= 1945:
    print("You are from the 'Silent Generation!'")
elif yrBorn >= 1946 and yrBorn <= 1964:
    print("You are a 'Baby Boomer'")
elif yrBorn >= 1965 and yrBorn <= 1980:
    print("You are a 'Generation-X'")
elif yrBorn >= 1981 and yrBorn <= 1996:
    print("Hah! Millenial! Avacado toast and Starbucks much!")
elif yrBorn >= 1997 and yrBorn <= 2012:
    print("You are from 'Generation-Z'")
elif yrBorn > 2012:
    print("You are 'Generation Alpha'")
else:
    print("You are...")
