# Scripts and files associated with the _C. bovis_ manuscript

### Calculating repeat density across a chromosome
We used the approach of [Berriman _et al._ (2018)](https://protocolexchange.researchsquare.com/article/nprot-6761/v1) to create repeat libraries for _C. bovis_ and _C. elegans_. These repeat library was then provided to [RepeatMasker](http://www.repeatmasker.org/) which generated a FASTA file with repeats masked with Ns. We then used `repeat_density.py` to calculate repeat density across each chromosome or contig like so: 

```
./repeat_density.py CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.scaffolds.fna.masked 50000
```

Where:

`CELEG.caenorhabditis_elegans_N2_PRJNA13758_WBPS12.scaffolds.fna.masked` = masked genome FASTA

`50000` = bin size
