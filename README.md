# Chamfer distance-based KNN for point cloud models comparison
This repository provides _Python_ implementation of _KNN_ algorithm for _point cloud_ models comparison by _Chamfer distance_

## Navigation
- `find_nearest.py` -- finds top nearest 3D models for target model
- `compare.py` -- compares two 3D models
- `show.py` -- shows 3D model from specified point cloud file
- `quick_run/` -- contains bash-scripts for quick running above scripts
- `models/` -- contains point cloud models

## Models
### Normal
<img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/bunny_normal.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/dragon_normal.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/vase_normal.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/cube_normal.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/sphere_normal.png" width="150">
### Diffused
<img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/bunny_diffused.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/dragon_diffused.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/vase_diffused.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/cube_diffused.png" width="150"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/sphere_diffused.png" width="150">

## Results
If we try to find closest _diffused_ model for _normal bunny_ model by running
```bash
python find_nearest.py models/normal/bunny.ply \
                       models/diffused/ \
                       -s 1000
```
we obrain next results:
```
K Nearest Models to models/normal/bunny.ply:
models/diffused/bunny_D02_L04.ply:      0.0021084902964208802
models/diffused/cube_D02_L04.ply:       0.004529813682506928
models/diffused/sphere_D02_L04.ply:     0.0054064578883468795
models/diffused/vase_D02_L04.ply:       0.029371351044122095
models/diffused/dragon_D02_L04.ply:     0.030610421838445444
```

Note that here we used only _1000_ random points from original model (~30k points) for improving computation speed.

So above results mean that for _subsampled_ target _normal bunny_ model

<img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/bunny_normal.png" width="100"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/arrow.png" width="90"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/bunny_normal_subset.png" width="100">

this algorithm performed next ranking on proposed _diffused_ models:

<img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/bunny_diffused.png" width="100"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/cube_diffused.png" width="100"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/sphere_diffused.png" width="100"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/vase_diffused.png" width="100"><!--
--><img src="https://github.com/Crowbar97/3D-KNN/blob/master/images/dragon_diffused.png" width="100">

## Sources
- :scroll: [3D ML. Часть 2: метрики качества и функции потерь в задачах 3D ML](https://medium.com/phygitalism/3d-ml-metrics-loss-functions-9708ff0476e2)
- :scroll: [C-LOG: A Chamfer distance based algorithm for localisation in occupancy grid-maps](https://www.sciencedirect.com/science/article/pii/S2468232216300555)
- :globe_with_meridians: 3D models were borrowed from [C-LOG: A Chamfer distance based algorithm for localisation in occupancy grid-maps](https://www.epfl.ch/labs/mmspg/downloads/geometry-point-cloud-dataset/)
