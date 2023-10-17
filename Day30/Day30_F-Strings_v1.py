#Title: Replit Day  - Day30 - F-String - F...What?! - v1

print("Survey and Feedback")
print("30 days down - what did you think?")

def scores_day1(score):
    align_center = 70
    if score > 5:
        print(f"{'You thought it was amazing!' : ^{align_center}}")
    elif score == 5:
        print(f"{'you thought it was OK?' : ^{align_center}}")
    else:
        print(f"{'you thought it was bad?!' : ^{align_center}}")

days = 1
for days in range(30 + 1):
      print(f"Day {days}:")
      day = input("What did you think about the lessons? (scale 1 to 10): ")
