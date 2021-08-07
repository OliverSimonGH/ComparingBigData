import os
import csv 
import time
import pandas as pd

from binary_tree import BinaryTree

emails = BinaryTree()
found = []

# Remove duplicate entries from txt file using set
# Write unique entries to a new file
def remove_duplicates():
    with open("emails.txt") as f:
        unique_lines = set([i[1:].lower() for i in f.readlines()])
    
    with open("uniques.txt", "w") as f:
        f.writelines(unique_lines)
    
# Process the CSV chunk    
# Change the data to match data in txt file (CSV to TXT)
def process(chunk):
    data = chunk.email
    
    for i in data:
        i = str(i).split("@")[0] + "@".strip()
        if len(i) > 2:
            # check if email exists in binary serach tree
            email_found = emails.find(i, i)
            if email_found is not None:
                email_found = email_found.__str__().split(",")[0].strip()
            
                if email_found == i:
                    if email_found not in found:
                        found.append(email_found)
                        with open("results.txt", "a") as l:
                            l.write(f"{email_found}\n")
                            continue

# Check if uniques.txt file exists
# if not run function remove_duplicates()
before = time.perf_counter()
if not os.path.isfile("uniques.txt"):
    remove_duplicates()

# Open uniques.txt and pass all the data to the binary tree (around 80,000 lines)
with open("uniques.txt") as f:
    for line in f.readlines():
        emails.insert(line.lower().strip(), line.lower().strip()) 

    # Balance the binary tree for quicker searches
    emails.balance()

# Open and read the CSV every 100,000 lines (CSV was massive being around 40GB, cant store it in memory as it's too big)
# had to compare uniques.txt to the test.csv and find a matching email, hence the BST
# BST increased perfomance dramatically vs an array
for chunk in pd.read_csv("test.csv", chunksize=100000, sep='\t'):
    process(chunk)

after = time.perf_counter() - before
print("[ENDED] finished the search in %.2f seconds\n" % after)
    
