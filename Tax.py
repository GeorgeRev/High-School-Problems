grossProfit = float(input("Enter your company's profit:"))
tax = (grossProfit / 100) * 30
netProfit = grossProfit - tax
print("Your tax due is:",tax,"and net profit is:",netProfit,".")