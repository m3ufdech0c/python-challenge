Python Challenge
=========================================
PyBank
========================================================================================
Upon importing the dependencies and establishing the path the relative file,
The script first reads into the file and stores the csv file header row into a variable named 'csv_header'. The script will skip this header row anytime rows are called.

Using the for loop, Script loops through all rows;
1- splits the 'date' column into 2 new separate columns 'day' and 'month' and stores there values into their respective lists
2- stores values of the 'profits/losses' column into the 'pnl' list

Within this 'For' loop we are using the 1st 'If' statement to calculate the difference between 2 subsequent profit/losses values and assign it to the 'change' list. In this process however, we want to skip the 1st row of that column (because '1088983' minus the initial value of the 'previous' variable '0' would be 1088983 and would skewed our total change). Therefore we declare the 1st row as boolean variable with a 'True' value and have the difference only calculated for the remaining rows, ie (isfirstrow == False). 

While doing the above, we are using 2 'If' statements (indented within the 1st one) to:
1- look for the highest positive change and store it in the variable 'maxchange, while reading the associated date and stores it in the 'maxchangedate' variable, or
2- look for the highest negative change and store it in the variable 'minchange, while reading the associated date and stores it in the 'minchangedate' variable

==================================================
PyPoll
==================================================
Upon importing the dependencies and establishing the path the relative file,
The script first reads into the file and stores the csv file header row into a variable named 'csv_header'. The script will skip this header row anytime rows are called.

Using the 'For' we are going through all rows, loking for the candidate names to store in the candidates dictionary (we chose a dictionary object over a list because each one of these candidates will need to be a key with different assigned values to be called upon later). 
In the process, We are using a 'previous candidate' variable with an empty string as its initial value, in order to grab the 1st candidate name encoutered in the 'candidate' column. The variable will then take on the value of the current row.

We are then using a second for loop to establish the winner. This time we are looping within the 'candidates' dictionary looking for the candidates key that has the max number of votes and when found assigning it as the winner. Aain using a variable 'max_votes' with initial value '0' to compare the first key to, but right after the first loop, setting its value to that previously found candidates key 
