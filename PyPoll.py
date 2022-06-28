# The data we need to retrieve
# 1. The total number\Recources\e\ of votes
# 2. A complete list of cadidates who got votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote


# Open the election results and read the file

import csv
import os

file_to_load = os.path.join('Election_Analysis','Recources','election_results.csv')

#Initialize the vote count at 0
total_votes = 0

#Candidate list
candidate_options = []

#Empty dictionary for votes per candidate
candidate_votes = {}

#Winning candidate trackers
winning_candidate = ''
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    #Perform analysis
    file_reader = csv.reader(election_data)

    # Read just the header
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        
        #Add votes to total votes
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list IF IT IS NOT already in the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0

        #add to that candidate's votes
        candidate_votes[candidate_name] += 1

#Iterate through the candidate names
for candidate_name in candidate_votes:

    #Retrieve voter count for each candidate
    votes = candidate_votes[candidate_name]

    #calculate the % votes
    vote_percentage = float(votes)/float(total_votes)*100

    #print the vote %
    #print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.')

    #to do: print out each candidate's name, vote count, and percent of votes to the terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    #Determine winning vote count and candidate

    #Determine if vote count is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-------------------------\n'
)

print(winning_candidate_summary)
    




#Create filename variable to a direct or indirect path to the file
file_to_save = os.path.join('Election_Analysis','Analysis','election_results.txt')
#use the open statement to open the file as writeable
with open(file_to_save,'w') as txtfile:

#Write some data to the file

    txtfile.write('Counties in the Election\n')
    txtfile.write('------------------------\n')    
    txtfile.write('Arapahoe\nDenver\nJefferson')
