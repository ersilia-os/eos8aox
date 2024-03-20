# imports
import os
import sys
import numpy as np
import numpy.typing as npt
import json
import csv
from typing import List

from signaturizer3d.space import CCSpace

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)

from model import FineTunedUniMol

# current file directory
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

DATASETS = ["A1", "A2", "A3", "B1", "B4", "C3"]

def get_model_path(ds):
    return os.path.join(checkpoints_dir, "{}_split3.pt".format(ds))


class Signaturizer:
    def __init__(self, space: CCSpace, model_file_url):
        if not isinstance(space, CCSpace):
            try:
                space = CCSpace[space]
            except KeyError:
                raise ValueError(
                    f"{space} is not a valid CCSpace. Valid spaces are A1 ... E5, see the CCSpace enum."
                )
        self.space = space
        self.model_file_url = model_file_url

        # Hydrogens are always removed as the signaturizers models are fine
        # tuned from the pre-trained UniMol model trained without hydrogens
        self.model = FineTunedUniMol(space=self.space, remove_hs=True, use_local_weights=True, model_file_url = self.model_file_url)

    def infer_from_smiles(self, smiles_list: List[str]) -> npt.NDArray[np.float32]:
        sig_output = self.model.get_sig4_smiles(smiles_list)
        return sig_output


ds = "A1"
path = get_model_path(ds)
signaturizer = Signaturizer(space=ds, model_file_url= path)
smiles_list = ['C', 'CCC', "CN(C)CCOC(C1=CC=CC=C1)C1=CC=CC=C1" ]
signatures = signaturizer.infer_from_smiles(smiles_list)
print(signatures.shape) # -> (3, 128) a 128D vector per molecule

def predict(smiles_list):
    res_ = {}
    for ds in DATASETS:
        path = get_model_path(ds)
        signaturizer = Signaturizer(space=ds, model_file_url= path)
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
