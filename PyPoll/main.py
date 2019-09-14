# PyPoll_Solution 

import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = 0
candidates = []
vote_count = {}
vote_percent = {}

with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
   for row in csvreader:
       votes = votes + 1
       candidate = row[2]
        
       if candidate not in candidates and candidate not in "Candidate":
           candidates.append(candidate) # add candidate to list of candidates
           vote_count[candidate] = 1  # in dictionary, assign 1 vote to this candidate
            
       elif candidate in candidates and candidate not in "Candidate":
           vote_count[candidate] = vote_count[candidate] + 1  # increment candidate's vote by 1
   

# Calculate percentage of votes
   for key, value in vote_count.items():
       vote_percent[key] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"

#    find the WINNER
   maxi = max(vote_count.keys(), key=(lambda k: vote_count[k]))

    
    #Variables needed to print results of election
   space = "-------------------------------"
   results1 = (
       "Election Results" + '\n' + space + '\n' + "Total Votes: "+ str(votes)+ '\n' + space + '\n')
   results2 = (
       space + '\n'
       "Winner: "+ str(maxi)+ '\n' + space + '\n')
 

# Print results of election
   print(results1)
   for key, val in vote_percent.items():
       print(key, ": ", val)
   print(results2)
  
# Create Output Text file
   text_file = open("PyPoll_Election_results.txt", "w")
   text_file.write(results1)
   for key, val in vote_percent.items():
        text_file.write((key + ": " + val)+ '\n')
   text_file.write(results2)

# close file
   text_file.close()