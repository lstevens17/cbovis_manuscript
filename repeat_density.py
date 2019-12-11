#!/usr/bin/env python2.7

from __future__ import division
import sys


def parse_fasta_file(fasta_file):
	with open(fasta_file, 'r') as fasta:
		fasta_dict = {}
		for line in fasta:
				if line.startswith(">"):
					header = line.rstrip("\n").replace(">", "")
					fasta_dict[header] = ''
				else:
					fasta_dict[header] += line.rstrip("\n")
	return fasta_dict

def count_Ns(fasta_dict, bin_size):
	for header, seq in fasta_dict.iteritems():
		start, end = 0, bin_size
		seqlen = len(seq)
		# print repeat density for each bin
		while start + bin_size < seqlen:
			N_count = seq[start:end].upper().count("N")
			print header, start, end, start/seqlen, N_count/(end - start)
			start += bin_size
			end += bin_size
		# print repeat density for last chunk of sequence that is small than bin size		
		N_count = seq[start:end].upper().count("N")
		print header, start, seqlen, start/seqlen, N_count/(seqlen - start) 

if __name__ == "__main__":
    SCRIPT = "repeat_density.py"
    try:
        fasta_file = sys.argv[1]
        bin_size = int(sys.argv[2])
    except IndexError:
        sys.exit("USAGE: ./%s %s %s" % (SCRIPT, "[genome.fa]", "[bin_size]"))
    fasta_dict = parse_fasta_file(fasta_file)
    count_Ns(fasta_dict, bin_size)
