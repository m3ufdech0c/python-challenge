import os
import csv

# Create a path to the PyBank csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store data
voters = []
candidates = {}
#income = []
#poverty_count = []
#poverty_rate = []
#county = []
#state = []

previous_candidate = ""

# Reads in the CSV for PyBank, stores the header row and skips it
with open(csvpath) as csvpypoll:
    csvreader = csv.reader(csvpypoll, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Add Ballot IDs to the 'Voters' list
        #voters.append(row[0])

        if row[2] != previous_candidate:
            if row[2] in candidates:
                candidates[row[2]] += 1
            else:
                candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
        previous_candidate = row[2]

total_votes = sum(candidates.values()) 

print("Election Results")
print("------------------------------------------------")
print(f"Total votes: {total_votes}")
print("------------------------------------------------")
max_votes = 0
winner = ""
for key in candidates.keys():
    if candidates[key] > max_votes:
        max_votes = candidates[key]
        winner = key
    print(f"{key}: {round(candidates[key]/total_votes*100, 3)}% ({candidates[key]})")
print("------------------------------------------------")
print(f"Winner: {winner}")

#print(f"Total Votes: {len(voters)}")


