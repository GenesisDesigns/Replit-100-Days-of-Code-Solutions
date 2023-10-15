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
        print(f"{'you thought it was SHIT?! WTF!' : ^{align_center}}")
