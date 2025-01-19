import sys
import pandas as pd
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1], sep="\t", header=None)
    df[2] = -3/4*np.log(1 - 4/3*df[2])
    df.pivot(index=0, columns=1, values=2).to_csv(sys.argv[2], sep="\t", float_format='%.7f')

