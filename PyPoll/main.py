# Eric Dowd PyBank Python Program

# Importing libraries for CSV and directory handling
import csv
import os


#load election file for analysis and assigning varabile
election_file = os.path.join("Resources", "election_data.csv")


#creating and initializing variables
total_votes=0

with open(election_file) as election_df:
    reader = csv.reader(election_df)

    #processing header row to exclude from calculation
    header = next(reader)
    first_row = next(reader)
    total_votes += 1
    
    for row in reader:
    	total_votes += 1



user_display = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n")

# display analysis to user on screen

print (user_display)

#save a text file of analysis to user
elect_results_file = os.path.join("analysis", "election_results.txt")

with open(elect_results_file, "w") as txt_file:
    txt_file.write(user_display)
