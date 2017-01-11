import pdb
from scipy.spatial import Delaunay
import sys
import pandas as pd
import numpy as np

# python chemical_hull.py "cloud.csv" "points.csv" "inside_hull"

cloud_raw = pd.read_csv(sys.argv[1])
cloud = cloud_raw.ix[:,1:8].as_matrix()
points_raw = pd.read_csv(sys.argv[2])
points = points_raw.as_matrix()
output_file_name = sys.argv[3]
hull = Delaunay(cloud)
output = hull.find_simplex(points)>=0
np.savetxt(output_file_name + ".csv", output, fmt="%5i")
