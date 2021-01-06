# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Initialize Candidate List
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        
        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate options list
            candidate_options.append(candidate_name)
    
        # Add to the toal vote count
        total_votes += 1

# Print the candidate options list
print(candidate_options)

# Print the total votes
print(total_votes)
