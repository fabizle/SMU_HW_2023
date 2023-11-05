import os
import csv

csvpath = "election_data.csv"
#variables
total_votes = 0
cand_dict = {}

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        print(row)


        total_votes += 1

        candidate = row[2]

        if candidate in cand_dict.keys():
            cand_dict[candidate] += 1
        else:
            cand_dict[candidate] = 1


print(total_votes)
print(cand_dict)


winning_votes = 0
winning_candidates = ""

for cand in cand_dict.keys():
    votes = cand_dict[cand]

    if votes > winning_votes:
        winning_votes = votes
        winning_candidates = cand

print (winning_candidates, winning_votes)



output = f"""
Election Results
Total Votes : {total_votes}
\n"""

for key in cand_dict.keys():
    perc = round(100*cand_dict[key]/total_votes, 3)
    newline = f"{key}: {perc}% ({cand_dict[key]})\n"
    output += newline

lastline = f"""

Winner: {winning_candidates}

"""

output += lastline
print(output)

with open("pypoll.txt", "w") as txt_file:
    txt_file.write(output)



