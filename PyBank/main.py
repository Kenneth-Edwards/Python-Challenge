# PyBank_Solution
import os
import csv


csvpath = os.path.join("..", "Resources", "budget_data.csv")

profit_loss_matrix = []
total = 0
total_months = 0

with open(csvpath, newline = '') as csvfile:
    budgetreader = csv.reader(csvfile,delimiter=',')
        
    # Skip header row
    next(budgetreader)
        
    # Convert budget_reader string to a list profit_loss_matrix
    # create a list called profit_loss_matrix to contain all data in budget_reader
    for line in budgetreader:
        profit_loss_matrix.append(line)
        
        # The cumulative total for "Profit/Losses" over the entire timeframe
        total += int(line[1])
        
        # The total number of months in the dataset
        total_months += 1
    
    subtract_MoM = 0
    CumulativeMoMChg = 0
    Avg_Chg_MoM = 0
    last_row_index = total_months-1
    
    last_month = profit_loss_matrix[last_row_index][0]
    last_month_PL = int(profit_loss_matrix[last_row_index][1])
    next_to_last_month_PL = int(profit_loss_matrix[last_row_index-1][1])
    
    last_delta = last_month_PL - next_to_last_month_PL
        
    min_month_yr= last_month
    max_month_yr= last_month
       
    min_delta = last_delta
    max_delta = last_delta
    
    # Calculate the delta of the profit/loss month to month over the entire period
    # iterate (backwards) from last month to the first month
    indexes = [i for i in range(total_months,1,-1)] # iteration will stop when i is 2

    for i in indexes: # stops when i is 2
        month = profit_loss_matrix[i-1][0]
        monthly_delta = int(profit_loss_matrix[i-1][1])-int(profit_loss_matrix[i-2][1])
        
        # Find the Greatest profit/loss Increase and Greatest  profit/loss Decrease over the entire period
        if monthly_delta < min_delta:  # if monthly_delta < min[1]:
            min_month_yr = month
            min_delta = monthly_delta
                        
        elif monthly_delta > max_delta:  # if monthly_delta > max[1]:
            max_month_yr = month
            max_delta = monthly_delta            
    
        # Cumulative total "Profit/Losses" of changes over the entire period
        CumulativeMoMChg += monthly_delta
    
    # Calculate the AVERAGE month-to-month delta for "Profit/Losses" over the entire period    
    Avg_Chg_MoM = CumulativeMoMChg/(total_months - 1)
        

'''
Desired Output
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''

textoutputfile='\\Users\\Owner\\GitHub\\Python-Challenge\\Pybank\\PyBank_Financial Analysis_Output.txt'
text_file=open(textoutputfile,"w")

# Output text file
text_file.write('PyBank Financial Analysis')
text_file.write('\n---------------------------------------------------')
text_file.write('\nTotal Months: ' + str(total_months))
text_file.write('\nTotal: $' + str(total))
text_file.write('\nAverage  Change: $' + str(round(Avg_Chg_MoM,2)))
text_file.write('\nGreatest Increase in Profits: ' + max_month_yr + ' ($' + str(max_delta) + ')')
text_file.write('\nGreatest Decrease in Profits: ' + min_month_yr + ' ($' + str(min_delta) + ')')
text_file.write('\n---------------------------------------------------')

# Output to screen/terminal
print('PyBank Financial Analysis')
print('---------------------------------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total))
print('Average  Change: $' + str(round(Avg_Chg_MoM,2)))
print('Greatest Increase in Profits: '+ max_month_yr + ' ($'+str(max_delta) + ')')
print('Greatest Decrease in Profits: '+ min_month_yr + ' ($'+str(min_delta) + ')')
print('---------------------------------------------------')

# Close text file
text_file.close()
