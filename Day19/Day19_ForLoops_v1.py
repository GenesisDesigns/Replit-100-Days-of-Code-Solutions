#Title: Replit Day  - Day19 - ForLoop - Let's be a bit Lazy - v1


print("Loan Calculator")
print("-------------------------")

principal_loan = 1000
APR = 0.05
yearExpiration = 10

for years in range(10):
  loanAndInterest = principal_loan * (1 + APR)**(years+1)
  loanAndInterest = round(loanAndInterest, 2)
  total_Interest = round(loanAndInterest - principal_loan, 2)
  print("Years", years+1, " loan ($): ", loanAndInterest, " InterestPmt ($): ", total_Interest )

print()
print(f"With an APR of {APR*100}% at year {yearExpiration}, you will owe a total interest of ${total_Interest}.")


  

  
