import sys
import argparse

import open3d as o3d

from utils import get_subset_model, read_models, read_model
from chamfer_dist import chamfer_dist


def find_nearest(target_model, models, subset_size=100):
    target_subset_model = get_subset_model(target_model, subset_size)
    dists = []
    for check_model in models:
        print('Checking %s...' % check_model.name)
        dists.append((check_model.name,
                      chamfer_dist(target_subset_model.pcd,
                                   check_model.pcd)))
        print('Dist: {}'.format(dists[-1]))
    return sorted(dists, key=lambda res: res[1])


def main():
    parser = argparse.ArgumentParser(description='Chamfer distance-based KNN')
    parser.add_argument('target_model_path', type=str,
                        help='path to point cloud file of target model')
    parser.add_argument('models_dir_path', type=str,
                        help='path to the check models directory')
    parser.add_argument('-s', '--subset', type=int,
                        help='use only subset of points of target model for KNN estimation')
    args = parser.parse_args()

    target_model = read_model(args.target_model_path)

    models = read_models(args.models_dir_path)

    subset_size = 100
    if args.subset:
        subset_size = args.subset
        print('subset size: %s' % subset_size)
    else:
        print('default subset size: %s' % subset_size)

    dists = find_nearest(target_model, models, subset_size)

    print('K Nearest Models to %s:' % args.target_model_path)
    for dist in dists:
        print('%s:\t%s' % dist)


main()



