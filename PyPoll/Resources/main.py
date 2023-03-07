#Import modules
import os #for file paths
import csv #csv files
import collections #for tuples
from collections import Counter

# Create a path to access csv file from resources folders
pypollCSV = os.path.join("..","Resources", "election.csv")
#Variables
candidates = [] #name of the candidates 
candidate_num_votes = [] #number of votes each candidate gets
votes_percentage = [] #percentage of votes
totalvotes= 0 #total number of votes for all candidates combined

#open csv and readi
with open(pypollCSV, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip the header
    next(csvreader)
    for row in csvreader:
        # Add to the total vote count
        totalvotes += 1

        # Get the candidate name from the row
        candidate_name = row[2]

        # If the candidate is new, add them to the list of candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            #candidate_num_votes[candidate_name]=0

            
        # Add one vote to the candidate's total vote count
        candidate_num_votes.append(candidate_name)

# Count the votes for each candidate
votes_per_candidate = dict(Counter(candidate_num_votes))

# Calculate the percentage of votes for each candidate
votes_percentage = [round((votes / totalvotes) * 100, 3) for votes in votes_per_candidate.values()]
winner_votes = max(votes_per_candidate,key= votes_per_candidate.get)
winner_candidate = winner_votes
print(winner_votes)

print(f"Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("--------------------------")
for candidate, percent, votes in zip(candidates, votes_percentage, votes_per_candidate):
    print(f"{candidate}: {percent:.3f}% ({votes_per_candidate[votes]})")
print(f"--------------------------")
print(f"Winner: {winner_candidate}")
print("--------------------------")


# text file
pypollCSV = os.path.join("..","Resources", "output.txt")
with open(pypollCSV, "a") as outfile:
    outfile.write("Election Results\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Total Votes: {str(totalvotes)}\n")
    outfile.write("--------------------------\n")
    for candidate, percent, votes in zip(candidates, votes_percentage, votes_per_candidate):
        outfile.write(f"{candidate}: {percent:.3f}% ({votes_per_candidate[votes]})\n")
        outfile.write("--------------------------\n")
    outfile.write(f"Winner: {winner_candidate}\n")
    outfile.write("--------------------------\n")



