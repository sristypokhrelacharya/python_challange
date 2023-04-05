#module for reading csv files
import os
import csv
#locating the path for the csv files
csv_path = os.path.join("..", "Resources", "election_data.csv")
#opening csv file
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#rows in csv file equals to, as there is header and row need to be counted from two
csv_reader =next(csv_reader)
