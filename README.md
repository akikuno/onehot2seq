[![licence](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![PyPI version](https://img.shields.io/badge/Install%20with-PyPI-brightgreen.svg?style=flat-square)](https://pypi.org/project/onehot2seq/)
[![install with bioconda](https://img.shields.io/badge/Install%20with-Bioconda-brightgreen.svg?style=flat-square)](https://anaconda.org/bioconda/onehot2seq)

## Description

`onehot2seq` is a command-line tool decoding a one-hot numpy array to DNA/RNA/protein sequences.  

To encode sequences to a one-hot numpy array, use `seq2onehot`.  
https://github.com/akikuno/seq2onehot


## Installation

You can install `onehot2seq` using pip or bioconda:

```bash
pip install onehot2seq
```

```bash
conda install -c bioconda onehot2seq
```


## Usage

```bash
onehot2seq [options] -t/--type <dna/rna/protein> -i/--input <in.npy> -o/--output <out.txt/fasta>
```

## Options

```bash
-a/--ambiguous: include ambiguous characters
-f/--format <txt/fasta>: output as a FASTA format (default: txt)
```

The ambigous characters are:
- `XBZJ` for amino acid
- `NVHDBMRWSYK` for DNA and RNA

The detail of ambiguous characters is described here:  
https://meme-suite.org/meme/doc/alphabets.html


The header IDs of FASTA format are sequential numbers (e.g. `>seq1`, `>seq2`)


## Examples

```bash
# Output DNA sequences
onehot2seq -t dna -i example/dna.npy -o dna.txt

# Output DNA sequences as a FASTA format
onehot2seq -t dna -f fasta -i example/dna.npy -o dna.fasta

# RNA sequences
onehot2seq -t rna -i example/rna.npy -o rna.txt

# Protein sequences
onehot2seq -t protein -i example/protein.npy -o protein.txt
```

## One-hot array

The input file must contain 3d one-hot array of `RxNxL` (Read x Nucreotide/Amino acid x Letter)

- The order of nucreotide is `ACGT` (+ `NVHDBMRWSYK`) for DNA, `ACGU` (+ `NVHDBMRWSYK`) for RNA
- The order of amino acid is `ACDEFGHIKLMNPQRSTVWY` (+ `XBZJ`)
