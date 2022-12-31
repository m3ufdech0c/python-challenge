import os
import csv

# Create a path to the PyBank csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Reads in the CSV for PyBank and stores the header row
with open(csvpath) as csvpybank:
    csvreader = csv.reader(csvpybank, delimiter=',')
    csv_header = next(csvreader)
    
    # Lists to store day and month from the upcoming split of the date column
    day = []
    month = []

    # Read each row of data after the header
    for row in csvreader:
        # Split the date into day and month
        split_date = row[0].split("-")
        day.append(split_date[0])
        month.append(split_date[1])
    print(f"Total Months: {len(month)}")    