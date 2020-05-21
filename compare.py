import sys
import argparse

import open3d as o3d

from utils import get_subset_model, read_models, read_model, view_model
from chamfer_dist import chamfer_dist


def compare(target_model, check_model, subset_size=500):
    target_subset_model = get_subset_model(target_model, subset_size)
    view_model(target_subset_model)

    view_model(check_model)

    dist = chamfer_dist(target_subset_model.pcd, check_model.pcd)
    print('Chamfer distance between\n\t%s\n\tand\n\t%s:\n%s'
          % (target_model.name, check_model.name, dist))


def main():
    parser = argparse.ArgumentParser(description='compares two point cloud models by Chamfer distance')
    parser.add_argument('target_model_path', type=str,
                        help='path to point cloud file of target model')
    parser.add_argument('check_model_path', type=str,
                        help='path to point cloud file of check model')
    parser.add_argument('-s', '--subset', type=int,
                        help='use only subset of points of target model for distance estimation')
    args = parser.parse_args()


    target_model = read_model(args.target_model_path)
    check_model = read_model(args.check_model_path)

    subset_size = 500
    if args.subset:
        subset_size = args.subset
        print('subset size: %s' % subset_size)
    else:
        print('default subset size: %s' % subset_size)

    compare(target_model, check_model, subset_size)


main()

