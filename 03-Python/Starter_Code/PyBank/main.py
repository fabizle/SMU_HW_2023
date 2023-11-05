import os
import csv

csvpath = "Resources/budget_data.csv"

total_months = 0
total_profit_loss = 0

changes = []
last_profit_loss = 0

max_change = -999999999
min_change = 999999999
max_month = ""
min_month = ""

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

  
    for row in csvreader:
        print(row)


        if total_months != 0:
            change = int(row[1]) - last_profit_loss
            changes.append(change)

        
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass

  
        last_profit_loss = int(row[1])

    
        total_months = total_months + 1

    
        total_profit_loss = total_profit_loss + int(row[1])

print(total_months)
print(total_profit_loss)

avg_change = sum(changes) / len(changes)
print(avg_change)

print(max_change)
print(max_month)
print(min_change)
print(min_month)


with open("output.txt", "w") as txt_file:
    output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    txt_file.write(output)