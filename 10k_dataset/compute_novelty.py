import sys
import pandas as pd

# read the distance matrix
dist = pd.read_csv(sys.argv[1], sep="\t")

dist[dist==0.00] = 999999

novelty_dict = {"query": [], "novelty": []}
diversity_dict = {"query": [], "diversity": []}
with open(sys.argv[2], 'r') as f: # read the tree list
    for line in f.readlines():
        qpath = "Demixing_Data/10k_dataset/" + line.strip()
        qpath += "/queries.txt"
        df = pd.read_csv(qpath, sep="\t", header=None)
        novelty = 0
        for i, r in df.iterrows():
            novelty += dist[r[0]].min() * r[1]
        novelty_dict["query"].append(line[3:].strip())
        novelty_dict["novelty"].append(novelty)

        diversity = 0
        for i, r1 in df.iterrows():
            for j, r2 in df.iterrows():
                if j < i:
                    diversity += dist.loc[r1[0]][r2[0]]
        diversity_dict["query"].append(line[3:].strip())
        diversity_dict["diversity"].append(diversity)

pd.DataFrame(diversity_dict).to_csv(sys.argv[3], sep="\t", index=None)
pd.DataFrame(diversity_dict).to_csv(sys.argv[4], sep="\t", index=None)
