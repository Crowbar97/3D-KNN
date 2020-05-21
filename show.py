import argparse

import open3d as o3d
import numpy as np

from model import Model
from utils import read_model, get_subset_model, view_model


parser = argparse.ArgumentParser()
parser.add_argument('path', type=str,
                    help='path to point cloud file')
parser.add_argument('-s', '--subset', type=int,
                    help='use only subset of points')
args = parser.parse_args()


model = read_model(args.path)

print(model.pcd)

if args.subset:
    model = get_subset_model(model, args.subset)

view_model(model)
