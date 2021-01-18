import os
import csv

#budget_csv = os.path.join('..','Resources','buget_data.csv')
budget_csv = r"C:\Users\Tiffany Yeh\NU-Bootcamp\python-challenge\PyBank\Resources\budget_data.csv"

#initializing variables
date_list = []
revenue_list = []
total_revenue = 0
calc_changes = 0
change_max = ['', 0]
change_min = ['', 0]

with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #total num of months included in the dataset
        date = row[0]
        revenue = float(row[1])
        date_list.append(date)
        #The net total amount of "Profit/Losses" over the entire period
        revenue_list.append(revenue)
        total_revenue += revenue
    net_revenue = (sum(revenue_list))
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        #check for greatest increase or decrease
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period
    total_months = len(date_list)
    for x in range(1, len(date_list)):
        change = revenue_list[x] - revenue_list[x - 1]
        calc_changes += change
        if change > change_max[1]:
            change_max = [date_list[x], change]
        if change < change_min[1]:
            change_min = [date_list[x], change]
    change_average = calc_changes / total_months

    one = 'Financial Analysis' + '\n'
    two = '-----------------------------------------------' + '\n'
    three = 'Total Months: ' + str(total_months) + '\n'
    four = 'Total: $' + str(net_revenue) + '\n'
    five = 'Average Revenue Change: $' + str(round(change_average)) + '\n'
    six = 'Greatest Increase in Revenue: ' + change_max[0] + ' ($' + str(round(change_max[1])) + ')' + '\n'
    seven = 'Greatest Decrease in Revenue: ' + change_min[0] + ' ($' + str(round(change_min[1])) + ')' + '\n'
    print(one + two + three + four + five + six + seven)

#write analysis to text file
Financial_Analysis = open("financial_analysis.txt",'w')
Financial_Analysis.write(one + two + three + four + five + six + seven)
Financial_Analysis.close()


