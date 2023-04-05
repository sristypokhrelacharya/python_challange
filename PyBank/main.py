#module for reading csv files
import os
import csv
#locating the path for the csv files
csvpath = os.path.join("Resources","budget_data.csv")
file_for_output = os.path.join ("python_challange\analysis")
#Declare the variables
total_months =[]
total_net_profits =[]
greatest_increase_profit = 0
greatest_increase_profit = []
greatest_decrease_profit = 0
greatest_decrease_profit = []
months_change = []
previous_value = 0
csvreader =any
i = []
#opening the csv file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimeter=",")
    #need to skip header so it wouldnot count as another month
    csv_reader = next(csvreader)

    for row in csvreader:
     #total of months and profit/losses
        total_months.append(row[0])
        total_net_profits.append(row[1])
    print(len (total_months))

#the net total profit and loss over the time period
total_profit_conv= [int(x)for x in total_net_profits]
total_net_profits = sum[total_profit_conv]
print(total_net_profits)

#now, calculating the changes of total profit over the time period
for i in range(len(total_net_profits)-1):
# taking the difference in months from deducting this year with preceeding years profit .
    months_change.append(total_net_profits(i+1)-total_net_profits[i])
print (total_profit_conv)
print(total_months)
print(total_net_profits)
