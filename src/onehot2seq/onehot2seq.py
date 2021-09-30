import sys
import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("input", help="numpy npy file", required=True)
args = parser.parse_args()

data_onehot = np.load(args.input)


def toACGT(data):
    seq = ""
    for i in range(len(data)):
        if data[i][0] == 1:
            seq += "A"
        elif data[i][1] == 1:
            seq += "C"
        elif data[i][2] == 1:
            seq += "G"
        elif data[i][3] == 1:
            seq += "T"
    return seq


seq = list()
for i in range(len(data_onehot)):
    seq.append(toACGT(data_onehot[i]))

pd.DataFrame(seq).to_csv(sys.stdout, header=None, index=None)
