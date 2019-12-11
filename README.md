# Scripts and files associated with the _C. bovis_ manuscript

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
