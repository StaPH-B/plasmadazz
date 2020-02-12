import os, sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def rotate_contig(sequence,ori_start):
    #if origin is at the start of the sequence don't rotate
    if(ori_start < 3):
        return sequence
    #adjust start for 0 index
    ori_start = ori_start - 1
    #get front and back chunk of DNA
    front_end = sequence[0:ori_start]
    back_end = sequence[ori_start:]
    #return sequence
    return back_end + front_end
