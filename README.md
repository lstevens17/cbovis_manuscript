# Scripts and files associated with the _C. bovis_ manuscript

### Recipricol best BLAST hits 
To define single-copy orthologues between _C. bovis_ and _C. elegans_, we used a recipricol best BLAST hit approach. We first filtered the protein FASTAs so that only the longest isoform of each gene was present. We then used BLASTP to search each proteome against the other like so:

```
blastp -query CBOVIS.caenorhabditis_bovis.v1.proteins.faa_longest_isoforms -db CBOVIS.caenorhabditis_bovis.v1.proteins.faa_longest_isoforms -outfmt '6 qseqid sseqid pident mismatch gapopen qstart qend sstart send evalue bitscore qcovs qcovhsp qlen slen length' -num_threads 16 >CBOVIS_vs_CELEG.blastp.txt
blastp -query CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.proteins.faa_longest_isoforms -db CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.proteins.faa_longest_isoforms -outfmt '6 qseqid sseqid pident mismatch gapopen qstart qend sstart send evalue bitscore qcovs qcovhsp qlen slen length' -num_threads 16 >CELEG_vs_CBOVIS.blastp.txt
```

We then provided these output files to a script written by Dom Laetsch (and available here https://github.com/DRL/GenomeBiology2016_globodera_rostochiensis) to define orthogues like so: 

```
./rbbh.py CBOVIS_vs_CELEG.blastp.txt CBOVIS.caenorhabditis_bovis.v1.proteins.faa_longest_isoforms CELEG_vs_CBOVIS.blastp.txt CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.proteins.faa_longest_isoforms 1e-25 75 >CBOVIS_CELEG.rbbh.txt
```

Where:

`1e-25` = minimum evalue for a hit to be considered
`75` = min query coverage for a hit to be considered

The output of this script is a TSV file showing the transcript IDs and BLAST results.

### Calculating repeat density across a chromosome
We used the approach of [Berriman _et al._ (2018)](https://protocolexchange.researchsquare.com/article/nprot-6761/v1) to create repeat libraries for _C. bovis_ and _C. elegans_. These repeat library was then provided to [RepeatMasker](http://www.repeatmasker.org/) which generated a FASTA file with repeats masked with Ns. We then used `repeat_density.py` to calculate repeat density across each chromosome or contig like so: 

```
./repeat_density.py CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.scaffolds.fna.masked 50000
```

Where:

`CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.scaffolds.fna.masked` = masked genome FASTA

`50000` = bin size

### Comparing gene structure between _C. bovis_ and _C. elegans_
We first need to extract stats for every transcript in each species using the GFF3 files. As part of the CGP, we have a standardised GFF3 format which makes life slightly easier. We calculated stats using `gene_structure_stats.py` like so: 

```
./gene_structure_stats.py CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.annotations.gff3`
```

Where:

`CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.annotations.gff3` = GFF3

The script produces a TSV file like the one below:

```
CELEG.F08H9.5	1846	5	1146	4	659	41	CELEG.WBGene00008593
```

Where the columns are:
1. transcriptID
2. transcript length
3. CDS count
4. CDS span 
5. intron count
6. intron span 
7. geneID

We can then use the output files in combination with a orthology clustering file to compare the gene structure in orthologous gene pairs. 
