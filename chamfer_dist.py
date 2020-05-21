from math import sqrt


def euc_dist(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2
                + (p2[1] - p1[1]) ** 2)


def find_closest_dist(p1, pcd):
    closest_dist = euc_dist(p1, pcd[0])
    for p2 in pcd:
        dist = euc_dist(p1, p2)
        if dist < closest_dist:
            closest_dist = dist
    return closest_dist


# here pcd means raw list of points
def chamfer_dist(pcd1, pcd2):
    dist = 0
    for i, p1 in enumerate(pcd1):
        if i % 10 == 0:
            print('%s / %s' % (i, len(pcd1)))
        dist += find_closest_dist(p1, pcd2)
    dist /= len(pcd1)
    return dist
