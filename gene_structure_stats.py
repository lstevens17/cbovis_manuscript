#!/usr/bin/env python2.7
import sys

def parse_gff3(GFF3_file):
	with open(sys.argv[1], 'r') as GFF3_file:
		transcript_to_gene = {}
		transcript_to_CDS_coords = {}
		transcript_to_CDS_lengths = {}
		transcript_lengths = {}
		for line in GFF3_file:
			if not line.startswith("#"):
				feature, start, stop, colnine = line.rstrip("\n").split("\t")[2], int(line.rstrip("\n").split("\t")[3]), int(line.rstrip("\n").split("\t")[4]), line.rstrip("\n").split("\t")[8]
				ID = colnine.split(";")[0].replace("ID=", "")
				if feature == 'transcript':
					ID = colnine.split(";")[0].replace("ID=", "")
					parent = colnine.split(";")[1].replace("Parent=", "")
					transcript_length = abs(start - stop) + 1
					transcript_lengths[ID] = transcript_length
					transcript_to_gene[ID] = parent
					transcript_to_CDS_coords[ID] = []
					transcript_to_CDS_lengths[ID] = []
				elif feature == 'mRNA':
					ID = colnine.split(";")[0].replace("ID=", "")
					parent = colnine.split(";")[1].replace("Parent=", "")
					transcript_length = abs(start - stop) + 1
					transcript_lengths[ID] = transcript_length
					transcript_to_gene[ID] = parent
					transcript_to_CDS_coords[ID] = []
					transcript_to_CDS_lengths[ID] = []
				elif feature == 'CDS':
					parent = colnine.split(";")[1].replace("Parent=", "")
					if "," in parent:
						parent = parent.split(",")[0]
					CDS_length = abs(start - stop) + 1
					transcript_to_CDS_lengths[parent].append(CDS_length)
					transcript_to_CDS_coords[parent].append(start)
					transcript_to_CDS_coords[parent].append(stop)
	return transcript_to_gene, transcript_to_CDS_coords, transcript_to_CDS_lengths, transcript_lengths

def create_output(transcript_to_gene, transcript_to_CDS_coords, transcript_to_CDS_lengths, transcript_lengths):
	for transcript, CDS_lengths in transcript_to_CDS_lengths.iteritems():
		CDS_span = 0
		for CDS_length in CDS_lengths:
			CDS_span += CDS_length
		CDS_coords = transcript_to_CDS_coords[transcript]
		if len(CDS_coords) > 0:
			start, stop = sorted(CDS_coords)[0], sorted(CDS_coords)[-1]
			transcript_length = transcript_lengths[transcript]
			CDS_and_intron_span = (abs(start - stop) + 1)
			CDS_count = len(CDS_lengths)
			intron_count = CDS_count - 1
			intron_span	= abs(CDS_and_intron_span - CDS_span)
			UTR_span = abs(transcript_length - CDS_and_intron_span)
			geneID = transcript_to_gene[transcript]
			print transcript + "\t" + str(transcript_length) + "\t" + str(CDS_count) + "\t" + str(CDS_span) + "\t" + str(intron_count) + "\t" + str(intron_span) + "\t" + str(UTR_span) + "\t" + geneID

if __name__ == "__main__":
    SCRIPT = "gene_structure_stats.py"
    try:
        GFF3_file = sys.argv[1]
    except IndexError:
        sys.exit("USAGE: ./%s %s" % (SCRIPT, "[GFF3_file]"))
    transcript_to_gene, transcript_to_CDS_coords, transcript_to_CDS_lengths, transcript_lengths = parse_gff3(GFF3_file)
    create_output(transcript_to_gene, transcript_to_CDS_coords, transcript_to_CDS_lengths, transcript_lengths)
