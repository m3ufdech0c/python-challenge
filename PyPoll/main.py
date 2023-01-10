import os
import csv

# Create a path to the PyBank csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# List and dictionary to store data
voters = []
candidates = {}
# Initializing value to an empty string
previous_candidate = ""

# Reads in the CSV for PyBank, stores the header row and skips it
with open(csvpath) as csvpypoll:
    csvreader = csv.reader(csvpypoll, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
       #Grabbing the name of the 1st candidate
        if row[2] != previous_candidate:
            # Making sure the same candidate is not stored twice, and increasing the candidate count by 1
            if row[2] in candidates:
                candidates[row[2]] += 1
            else:
                candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
        # Re-assigning the value of 'previous_candidate' as that of the current row
        previous_candidate = row[2]
#Counting the number of votes for each candidate and adding it as a value to the appropriate key in the dictionary
total_votes = sum(candidates.values()) 

# Set variable for output file and open it in write mode
output_file = open("Analysis/main_pypoll.txt","w")

# Creating variables to be commonly used between print and text file writing
title = "Election Results" 
votes = f"Total votes: {total_votes}"
line_separator = "------------------------------------------------"

# Priting lines to be displayed and writing on the output file
print(title)
output_file.write(title + "\n")

print(line_separator)
output_file.write(line_separator + "\n")

print(votes)
output_file.write(votes + "\n")

print(line_separator)
output_file.write(line_separator + "\n")

# Initializing variables to be used in the next loop
max_votes = 0
winner = ""
# Looing through the candidates and comparing their vote counts
for key in candidates.keys():
    if candidates[key] > max_votes:
        max_votes = candidates[key]
        winner = key
    # Computing vote count percentage and assigning it to the appropriate key with the candidates dictionary
    candidate_result = f"{key}: {round(candidates[key]/total_votes*100, 3)}% ({candidates[key]})"    
    print(candidate_result)
    output_file.write(candidate_result + "\n")

print(line_separator)
output_file.write(line_separator + "\n")

displaywinner = f"Winner: {winner}"
print(displaywinner)
output_file.write(displaywinner + "\n")

print(line_separator)
output_file.write(line_separator + "\n")

output_file.close()





