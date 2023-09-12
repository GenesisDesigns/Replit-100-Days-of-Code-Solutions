#Title: Replit Day  - Day21 - MathFacts - Throwback To Math Facts - v1

print("Math Game")
print("-----------------")
print()

multiples = int(input("Name your multiples: "))
start = 1
stop = 5
score = 0

for i in range(start, stop):
    correctAnswer = i * multiples
    print()
    yourAnswer = int(input(f"{i} x {multiples} = "))
    print()
    if yourAnswer == correctAnswer:
        print("Great!")
        score += 1
    else:
        print(f"Not quite. The correct answer is: {correctAnswer}")
