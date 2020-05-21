import sys
import os
import glob

import open3d as o3d
import numpy as np

from model import Model


def get_subset_model(model, subset_size=100):
    subset_point_ids = np.random.randint(0, len(model.pcd), subset_size)
    return Model(model.name + ' (subset)',
                 o3d.utility.Vector3dVector(model.pcd[subset_point_ids]))


def read_model(pcd_path):
    return Model(pcd_path,
                 np.asarray(o3d.io.read_point_cloud(pcd_path).points))


def read_models(pcds_dir_path):
    paths = glob.glob(os.path.join(pcds_dir_path, '*.ply'))
    print(paths)
    models = []
    for path in paths:
        models.append(Model(path, o3d.io.read_point_cloud(path).points))
    return models


def view_model(model):
    o3d_pcd = o3d.geometry.PointCloud()
    o3d_pcd.points = o3d.utility.Vector3dVector(model.pcd)
    o3d.visualization.draw_geometries([o3d_pcd])
