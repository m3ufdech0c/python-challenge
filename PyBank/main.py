import os
import csv
from statistics import mean

# Create a path to the PyBank csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reads in the CSV for PyBank, stores the header row and skips it
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
      
    # Creating variables to be commonly used between print and text file writing
    title = "Financial Analysis"
    months = f"Total Months: {len(month)}"
    total = f"Total: ${sum(pnl)}"
    avgchange = f"Average Change: ${round(mean(change), 2)}"
    maxchange = f"Greatest Increase in Profits: {maxchangedate} (${maxchange})"
    minchange = f"Greatest Decrease in Profits: {minchangedate} (${minchange})"
    
    print(title)

    print("------------------------------------------------------")

    print(months)
    print(total)
    print(avgchange)
    print(maxchange)   
    print(minchange) 

    # Set variable for output file and open it in write mode
    output_file = open("Analysis/main_pybank.txt","w")

    # Store some of the text lines inside a variable called "L"
    L = [months + "\n", total + "\n", avgchange + "\n", maxchange +"\n", minchange + "\n"]
    
    # priting lines on the file
    output_file.write(title + "\n")
    output_file.write("-------------------------------------------- \n")
    output_file.writelines(L)
    output_file.close()