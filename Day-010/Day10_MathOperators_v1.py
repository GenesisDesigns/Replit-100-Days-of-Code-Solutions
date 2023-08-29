#Title: Replit Day  - Day10 - Show me The Money - Math Operators (+, -, /, %, etc) - v1

totalBill = float(input("What was the total bill?: "))
tip = float(input("What percentage do you want to tip (decimals)?: "))
numberOfPpl = int(input("How many people?: "))
answer = (totalBill * (1+tip))/numberOfPpl
rndAnswer = str(round(answer, 2))
dollars = "$" + rndAnswer
print("You each owe: " + dollars)
