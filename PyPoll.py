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

with open(file_to_load) as election_data:

    #Perform analysis
    file_reader = csv.reader(election_data)

    # Print just the header

    headers = next(file_reader)
    print(headers)







#Create filename variable to a direct or indirect path to the file
file_to_save = os.path.join('Election_Analysis','Analysis','election_results.txt')
#use the open statement to open the file as writeable
with open(file_to_save,'w') as txtfile:

#Write some data to the file

    txtfile.write('Counties in the Election\n')
    txtfile.write('------------------------\n')    
    txtfile.write('Arapahoe\nDenver\nJefferson')
