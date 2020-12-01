
# Eric Dowd PyBank Python Program
# Importing libraries for CSV and directory handling
import csv
import os

#load budget file for analysis and assigning varabile
budget_file = os.path.join("Resources", "budget_data.csv")



#creating and initializing variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_total = 0

# using reader function to read file and store into a data frame
with open(budget_file) as budget_df:
    reader = csv.reader(budget_df)

    #processing header row to exclude from calculation
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_total += int(first_row[1])
    prev_net = int(first_row[1])

    #processing each row after the header and addig to total months and total while tracking greatest increast and greatest decrease in profit
    for row in reader:
    
        total_months += 1
        total_total += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#average change now calculated after all rows processed
avg_change = sum(net_change_list) / len(net_change_list)




# storing output display into a variable
user_display = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_total}\n"
    f"Average  Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# display analysis to user on screen
print(user_display)

#save a text file of analysis to user
analysis_file = os.path.join("analysis", "budget_analysis.txt")

with open(analysis_file, "w") as txt_file:
    txt_file.write(user_display)
