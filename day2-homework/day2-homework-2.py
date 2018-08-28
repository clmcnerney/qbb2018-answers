#!/usr/bin/env python3

import sys

fly_dict = {}
#make empty dictionary to fill later with fly ID as key and uniprot ID as value

def dict_maker(fname):
    #this function will set up the fly_dict to run against the ctab file using internal references 
    for line in open(fname):
        if "DROME" and "FBgn" in line:
            #these two conditions must be true for there to be a fly gene ID as well as being from the correct species
            fields = line.rstrip("\r\n").split()
            #strip and split the lines to define the fields
            fly_dict[fields[3]] = fields[2]
            #add to dictionary with field 3 (fly gene ID) as key and field 2 (uniprot ID) as value
            
def combo_maker(fname):
    #this function will run the comparison and print the resulting lines of matched (or not matched) data
    for line in open(fname):
        if "FBgn" in line:
            #skips the header line, which is the only line that doesn't contain the fbgn designation
            fields = line.rstrip("\r\n").split()
            #define fields
            if fields[8] in fly_dict.keys():
            #fields 8 is the same fly gene ID that is in the key of the dictionary - so if a match is found....
                print(fly_dict[fields[8]], "\t", line)
                #the script will print the uniprot ID value, a tab deliniation, and then the remainder of the line, basically appending the uniprot ID to the original ctab file for the matching cases
            else:
                if sys.argv[3] == "skip":
                    print ("\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t")
                elif sys.argv[3] == "fill":
                    print("No Uniprot ID", "\t", line)
                #what happens to the non-matching cases depends on argument 3. user has a choice of two words, skip is used, a blank line will replace the ctab line. If argument 3 is inputted as the word fill, the text "No Uniprot ID" will be printed as a placeholder in front of the ctab line data
                
output1 = dict_maker(sys.argv[1])
output2 = combo_maker(sys.argv[2])
#these tell the rest of the program what files to read for each function to run through
#argument 1 should be the text file from uniprot.org
#argument 2 should be the ctab file