# imports
import os
import sys
import numpy as np
import numpy.typing as npt
import json
import csv
from typing import List


from signaturizer3d import CCSpace, Signaturizer

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)


# current file directory
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

DATASETS = ["A1", "A2", "A3", "B1", "B4", "C3"]

def get_model_path(ds):
    return os.path.join(checkpoints_dir, "{}_split3.pt".format(ds))


def predict(smiles_list):
    res_ = {}
    for ds in DATASETS:
        path = get_model_path(ds)
        signaturizer = Signaturizer(space=ds, local_weights_path= path)
        signatures = signaturizer.infer_from_smiles(smiles_list)
        res_[ds]=signatures
    result = []
    for i in range(len(smiles_list)):
        d = {}
        for k, v in res_.items():
            d[k] = list([float(x) for x in v[i]])
        result += [d]
    output = {
        'result': result,
        'meta': None
    }
    return output

with open(input_file, "r") as f:
    smiles = []
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

data = predict(smiles)

with open(output_file, "w") as f:
    json.dump(data, f, indent=4)
