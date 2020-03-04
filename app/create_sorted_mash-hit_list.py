#! /usr/bin/python3
#Dependencies: python3, mash
#two args must be given:
#    1. [plasmid].fasta
#    2. plasmid_mash_database.msh
import os, sys, csv, subprocess, operator

#make sketch of fasta with mash
def mash_sketch(fasta):
    subprocess.run(["mash", "sketch", fasta])
    #print(fasta_sketch)
    #return fasta_sketch

#perform mash dist, output to file named plasmid_compare_mash.tsv
def mash_dist(fasta_msh, mash_db):
    with open("plasmid_compare_mash.tsv", "w") as file:
        subprocess.run(["mash", "dist", mash_db, fasta_msh], stdout=file)

def sort_on_third_element(list_of_lists):
    list_of_lists.sort(key = lambda x: x[2])
    return list_of_lists

#fasta of plasmid = plasmid_input
plasmid_input = sys.argv[1]
#mash db of plasmids for comparison = plasmid_mash_dict
plasmid_mash_dict = sys.argv[2]

fasta_sketch_file = mash_sketch(plasmid_input)
mash_dist(str(plasmid_input)+".msh", plasmid_mash_dict)

#convert mash tsv into a list of lists
with open("plasmid_compare_mash.tsv", "r") as mash_file:
    lines = csv.reader(mash_file)
    hits = list(list(rec) for rec in csv.reader(mash_file, delimiter='\t'))

sorted_hits = sort_on_third_element(hits)

#write the list of lists as a tsv file
with open("sorted_plasmd_comp_mash.tab", "w") as sorted_file:
    for item in sorted_hits:
        sorted_file.write('\t'.join(item))
        sorted_file.write('\n')

os.remove(str(plasmid_input)+".msh")
os.remove("plasmid_compare_mash.tsv")
