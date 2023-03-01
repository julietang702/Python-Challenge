import os
import csv    
#Path to collect data from the resources folder
pybankCSV = os.path.join("..","Resources", "budget_data.csv")
print(pybankCSV)
# Create Variables
months = []
profit_loss_delta = []
total_months = 0 
net_total_amount = 0
max_inc_profit=0
max_month = ""
min_dec_profit = 0
min_month= ""



#Read the CSV file
with open(pybankCSV, newline="") as csvfile:
    pybankCSV = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    next(pybankCSV)

    #Create Loop
    for row in pybankCSV:

        #append months
        months.append(row[0])

        #extend profit/loss change, row 1 is for the profit/loss column
        profit_loss_delta.append(int(row[1])) #convert to integer

#Find total amount of months in the data set
total_months = (len(months))

#total take home for profit/loss using sum function
net_total_amount = int(sum(profit_loss_delta))

#Average change for each month
average_delta = net_total_amount / total_months

#Greatest increase in profits using max function and find the date
max_inc_profit = max(profit_loss_delta)

index_max = profit_loss_delta.index(max_inc_profit) #date
max_month = months[index_max]

#Calculate the greatest decrease in loss (date and amount)
min_dec_profit = min(profit_loss_delta)
index_min = profit_loss_delta.index(min_dec_profit) #date
min_month = months[index_min]

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount:.2f}")
print(f"Average Change: {average_delta:.2f}")
print(f"Greatest Increase in Profits: {max_month} {max_inc_profit:.2f}")
print(f"Greatest Decrease in Profits: {min_month} {min_dec_profit:.2f}")


#Create a txt file 
pybankCSV= os.path.join("..", "Resources", "budget_data3.txt")
with open(pybankCSV, "a") as outfile:
    outfile.write(f"Financial Analysis")
    outfile.write(f"----------------------------")
    outfile.write(f"Total Months: {total_months} ")
    outfile.write(f"Total: ${net_total_amount:.2f} ")
    outfile.write(f"Average Change: {average_delta:.2f} ")
    outfile.write(f"Greatest Increase in Profits: {max_month} (${max_inc_profit:.2f})\n")
    outfile.write(f"Greatest Decrease in Profits: {min_month} (${min_dec_profit:.2f})\n ")

outfile.close()