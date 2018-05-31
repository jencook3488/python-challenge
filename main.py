import pandas as pd
from collections import Counter

df = pd.read_csv('election_data_1.csv')

cand = set(df['Candidate'])
candidates = [x for x in cand]
i = 0

votes = []
while len(votes) < len(candidates):
    votes.append(0)

while i < (len(candidates)):
    for c in df['Candidate']:
        if str(c) == candidates[i]:
            votes[i] +=  1
    i += 1           

total_votes = len(df['Voter ID'])

idx = votes.index(max(votes))
def output_file():
    print('Election Results')
    print("-------------------------")
    print("Total Votes: ", total_votes)
    print("-------------------------")
    for i in range(len(candidates)):
        vote_percentage = round(((votes[i]/total_votes)*100),2)
        print(str(candidates[i]) + ": " + str(vote_percentage) + "% " + "(" + str(votes[i]) + ")")
    print("-------------------------")
    print("Winner:", candidates[idx])
    print("-------------------------")

type(output_file)
output_func = str(output_file())

with open('text_file.txt', 'w') as text_file:
    text_file.write('Election Results \n') 
    text_file.write("-------------------------\n")
    text_file.write("Total Votes: ")
    text_file.write(str(total_votes) + "\n")
    text_file.write("-------------------------\n")
    for i in range(len(candidates)):
        vote_percentage = round(((votes[i]/total_votes)*100),2)
        text_file.write(str(candidates[i]) + ": " + str(vote_percentage) + "% " + "(" + str(votes[i]) + ")\n")
    text_file.write("-------------------------\n")
    text_file.write("Winner:" + candidates[idx] + "\n")
    text_file.write("-------------------------\n")

text_file.close()
