import metrics
from metrics.modularity import modularity
from metrics.z_diff import z_diff
from metrics.mig_sup import mig_sup
from metrics.dci import dci
#,z_diff,mig_sup,dci
import argparse
import numpy as np
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--features', help='features path')
parser.add_argument('--labels', help='labels path')
parser.add_argument('--out',help='labels path')
args = parser.parse_args()
feat_path=args.features
lbl_path=args.labels
out_path=args.out
feat_tensor=np.load(feat_path)
lbl_tensor=np.load(lbl_path)
modularity_score=modularity(lbl_tensor,feat_tensor)
#z_diff_score=z_diff(lbl_tensor,feat_tensor)
#mig_sup_score=mig_sup(lbl_tensor,feat_tensor)
#dci_score=dci(lbl_tensor,feat_tensor)
with open(out_path,"w") as f:
    f.write(f"{str(labels_tensor)}")
print(labels_tensor)
