
#import poll
#module for reading csv files
import os
import csv
#locating the path for the csv files
csv_path = os.path.join('Resources','election_data.csv')
#opening csv file
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#rows in csv file equals to, as there is header and row need to be counted from two
    csv_header =next(csv_reader)
    print (f"header:{csv_header}")


#declearing the variables
    ballot= []
    county=[]
    candidate=[]
    Charles_Casper_Stockham= []
    Diana_DeGette=[]
    Raymon_Anthony_Doane =[]
    Charles_Casper_Stockham_ballot =0
    Diana_DeGette_ballot =0
    Raymon_Anthony_Doane_ballot=0
#read each row of the dataset after header function
for row in csv_reader:
    ballot.append(int(row[0]))
    county.append(row[1])
    candidate.append(row[2])
#counting the ballets in the set 
    total_ballot= (len(ballot))
    #print (total_ballot)

#counting votes by each candidates:
for candidate in candidate:
    if candidate == "Charles casper stockham":
        Charles_Casper_Stockham.append(candidate)
        Charles_Casper_Stockham_ballot=len(Charles_Casper_Stockham)
        
    elif candidate=="Diana DeGette":
        Diana_DeGette.append(candidate)
        Diana_DeGette_ballot=len(Diana_DeGette)

    else:
        candidate== "Raymon_Anthony_Doane"
        Raymon_Anthony_Doane.append(candidate)
        Raymon_Anthony_Doane_ballot= len(Raymon_Anthony_Doane)

#print (Charles_Casper_Stockham_ballot)
#print(Diana_DeGette_ballot)
#print (Raymon_Anthony_Doane_ballot)

#for the percentage of ballots counts
    Charles_Casper_Stockham_percent=round(((Charles_Casper_Stockham_ballot/total_ballot)*100),2)
    Diana_DeGette_percent=round(((Diana_DeGette_ballot/total_ballot)*100),2)
    Raymon_Anthony_Doane_percent=round(((Raymon_Anthony_Doane_ballot/total_ballot)*100),2)
#print(Charles_Casper_Stockham_percent)
#print(Diana_DeGette_percent)
#print(Raymon_Anthony_Doane_percent)

#maximum ballets among candidates
if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
    Winner="Charles_Casper_Stockham"
elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent,Raymon_Anthony_Doane_percent):
    Winner="Diana_DeGette"
else:
    Winner= "Raymon_Anthony_Doane"
    #print statements
    
