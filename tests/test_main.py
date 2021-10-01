from src.onehot2seq.main import define_alphabet
from src.onehot2seq.main import decode_to_seq
from src.onehot2seq.main import format_to_fasta
import dataclasses
import numpy as np


@dataclasses.dataclass
class Args:
    input: str
    output: str
    type: str
    ambiguous: bool


args = Args("input", "output", "type", True)


def test_dna_fasta():
    data_eval = np.loadtxt("tests/dna.fasta", dtype=object)
    args.input = "example/dna.npy"
    args.type = "dna"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    output = format_to_fasta(seq)
    np.equal(np.array(output, dtype=object), data_eval)


def test_dna_txt():
    data_eval = np.loadtxt("tests/dna.txt", dtype=object)
    args.input = "example/dna.npy"
    args.type = "dna"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    np.equal(np.array(seq, dtype=object), data_eval)


def test_protein_fasta():
    data_eval = np.loadtxt("tests/protein.fasta", dtype=object)
    args.input = "example/protein.npy"
    args.type = "protein"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    output = format_to_fasta(seq)
    np.equal(np.array(output, dtype=object), data_eval)


def test_protein_txt():
    data_eval = np.loadtxt("tests/protein.txt", dtype=object)
    args.input = "example/protein.npy"
    args.type = "protein"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    np.equal(np.array(seq, dtype=object), data_eval)


def test_rna_fasta():
    data_eval = np.loadtxt("tests/rna.fasta", dtype=object)
    args.input = "example/rna.npy"
    args.type = "rna"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    output = format_to_fasta(seq)
    np.equal(np.array(output, dtype=object), data_eval)


def test_rna_txt():
    data_eval = np.loadtxt("tests/rna.txt", dtype=object)
    args.input = "example/rna.npy"
    args.type = "rna"
    args.ambiguous = False
    onehot = np.load(args.input)
    alphabet = define_alphabet(args.type, args.ambiguous)
    seq = decode_to_seq(onehot, alphabet)
    np.equal(np.array(seq, dtype=object), data_eval)
