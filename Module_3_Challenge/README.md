# Election Audit

## Overview of Election Audit
The purpose of this project is to execute an audit of the recently run 
election.  We'll use a .csv file containing the individual ballot choices per candidate
and county and audit the vote totals and percentages using a bespoke Pyhton program.
These results will be formatted and output to the terminal screen, as well as the election_analysis.txt file
in the /analysis folder of this project

## Election Audit Results
Our election audit Python program takes the .csv file containing the ballot information and 
executes business logic needed to perform the following calculations
- Total number of votes cast
- Total number of votes cast in each County
- Total percentage of the total votes cast per County
- County with the largest number of votes cast
- Total number of votes cast per candidate
- Percentage of the total votes per candidate
- Winning Candidate
- Winning Vote Count
- Winning Vote Percentage

### Results
![alt text](https://github.com/brian-mcrae/Election_Analysis/blob/main/Module_3_Challenge/analysis/election_analysis.PNG)

# Election Audit Summary
This program was designed for re-use and re-purposing, and 
can be used for any election to capture the same data, as the county and 
candidate lists are not hard-coded but rather populated from the raw data.
Business logic can also be changed or added to this script to enable analysis on 
other points.  For example, we might want to know what candidate and/or county received the 
LEAST number of votes.  To do so, we could simply re-use the logic that currently checks for the 
highest number of ballots cast per county and for each candidate and check/store for the lowest 
rather than the highest total.  We could also check to see if any candidates receieved zero votes, 
and if necessary remove that candidate from the results list.  We could accmoplish this by checking that
the vote totals for each candidate in our dictionary are greather than zero.
