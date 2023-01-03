import os
import csv
from statistics import mean

# Create a path to the PyBank csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reads in the CSV for PyBank and stores the header row
with open(csvpath) as csvpybank:
    csvreader = csv.reader(csvpybank, delimiter=',')
    csv_header = next(csvreader)
    
    # Lists to store data we will need to loop through
    day = []
    month = []
    pnl = []
    losses = []
    change = []
    # Initializing variable 'previous' to be used for computing changes withing the 'PnL' list
    previous = 0 
    isfirstrow = True
    maxchange = 0
    minchange = 0

    # Read each row of data after the header
    for row in csvreader:
        # Split the date column into day and month data to append to their respective lists
        split_date = row[0].split("-")
        day.append(split_date[0])
        month.append(split_date[1])

        # Add PnL data
        pnl.append(int(row[1]))
        
        # Here we are adding data to the "Change" list starting from row#2, while computing the differences between subsequent elements of the 'PnL' list
        if isfirstrow == False:
            change.append(int(row[1]) - previous)
            # Looping through the change list to find the maximum value by using the max() function and comparing it to the initial value of maxchange, notice 
            if max(change) != maxchange:
                maxchange = int(row[1]) - previous
                # Assigning the date for that instance where the change is the greatest as the maxchange date
                maxchangedate = row[0]
            # Looping through the change list to find the min value by using the min() function and comparing it to the initial value of minchange, notice 
            if min(change) != minchange:
                minchange = int(row[1]) - previous
                minchangedate = row[0]

    

        previous = int(row[1])

        isfirstrow = False
      
    # This could have been used to create the 'Change' but did not want another loop
    #for i in range(1, len(pnl)):
        #value = pnl[i] - pnl[i - 1]
        #change.append(value)
    
    print("Financial Analysis")

    print("------------------------------------------------------")

    print(f"Total Months: {len(month)}")
    print(f"Total: ${sum(pnl)}")
    print(f"Average Change: ${round(mean(change), 2)}")
    print(f"Greatest Increase in Profits: {maxchangedate} (${maxchange})")   
    print(f"Greatest Decrease in Profits: {minchangedate} (${minchange})") 