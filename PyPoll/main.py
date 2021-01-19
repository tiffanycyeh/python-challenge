import os
import csv

election_csv = r"C:\Users\Tiffany Yeh\NU-Bootcamp\python-challenge\PyPoll\Resources\election_data.csv"

#initializing variables
voter_list = []
candidate_list = []
roster = {}
winner = 0

#Opening file and reading in lines to count voters and number of candidates
with open(election_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        vote = row[0]
        voter_list.append(vote)
        candidate = row [2]
        if not candidate in candidate_list:
            candidate_list.append(candidate)
        if not candidate in roster:
            roster[candidate] = 1
        else:
            roster[candidate] += 1
#print(roster)
#Calculating Election Results
total_votes = float(len(voter_list))
vote_percentage = {candidate : roster[candidate]/total_votes for candidate in candidate_list}
print(vote_percentage)

#getting the key with maximum value in dictionary roster
max_key = max(roster, key=roster.get)
#print(max_key)

#summary printed out
print('Election Results')
print('------------------------------------------')
print('Total Votes: ' + str(int(total_votes)))
print('------------------------------------------')
for candidate in candidate_list:
    #print(str(vote_percentage[item]) + str(item) + ": " + '(' + str(roster[item]) + ')')
    print(str(candidate) + ': ' + str(vote_percentage[candidate]) + '% (' + str(roster[candidate]) + ')')

print('------------------------------------------')
print('Winner: ' + str(max_key))
print('------------------------------------------')

#summary stored in values for output file
one = 'Election Results'  + '\n'
two = '------------------------------------------'  + '\n'
three = 'Total Votes: ' + str(int(total_votes)) + '\n'
four = '------------------------------------------' + '\n'
results = []
for candidate in candidate_list:
    #print(str(vote_percentage[item]) + str(item) + ": " + '(' + str(roster[item]) + ')')
    results.append(str(candidate) + ': ' + str(vote_percentage[candidate]) + '% (' + str(roster[candidate]) + ')')
six = '------------------------------------------' + '\n'
seven ='Winner: ' + str(max_key) + '\n'
eight ='------------------------------------------' + '\n'

with open("election_results.txt", 'w') as f:
    f.write('Election Results' + '\n')
    f.write('------------------------------------------' + '\n')
    f.write(('Total Votes: ' + str(int(total_votes))) + '\n')
    f.write('------------------------------------------' + '\n')
    for dude in results:
        f.write(dude + '\n')
    f.write('------------------------------------------' + '\n')
    f.write('Winner: ' + str(max_key) + '\n')
    f.write('------------------------------------------' + '\n' )
    f.close()


#Election_Results = open("election_results.txt",'w')
#for dude in results:
#    Election_Results.write(dude)
#Election_Results.close()
#save to output text file
#Election_Results = open("election_results.txt",'w')
#Election_Results.write(one + two + three + four + five + six + seven + eight)
#Election_Results.close()





