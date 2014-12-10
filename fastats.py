#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File    	: fastats.py
Author  	: Dominik R. Laetsch, dominik.laetsch at gmail dot com 
Version 	: 0.1
Description : takes a fasta file and returns per contig gc, len (tab sepoarated)
To do 		: ...
"""

from __future__ import division
import sys, time

def parse_seqs_count(infile):
	
	'''Parses fasta file and returns the names of the contigs.'''

	header, seq = '', ''
	print "# header " + delim + "Uncorrected len" + delim + "Ns (%)" + delim + "ATGCs" + delim + "GC (%)"
	with open(infile) as fh:
		for line in fh:
			if line.startswith(">"):
				if (seq):
					print_data_count(header, seq)
					seq = ''	
				header = line.rstrip("\n")
			else:
				seq += line.rstrip("\n")
		print_data_count(header, seq)		

def print_data_count(header, string):
	seq = string.upper()
	uncor_length = len(seq)
	n_count = string.count('N')
	n_perc = n_count / uncor_length
	length = uncor_length - n_count
	gc = ( ( string.count('G') + string.count('C') ) / length )
	print header + delim + str(uncor_length) + delim + format(n_perc,'.3') + delim + str(length) + delim + format(gc,'.3') 

if __name__ == "__main__":
	try:
		infile = sys.argv[1]
	except:
		sys.exit("Usage: ./fastats.py [FASTAFILE]")
	delim = "\t"
	start = time.time()
	parse_seqs_count(infile)