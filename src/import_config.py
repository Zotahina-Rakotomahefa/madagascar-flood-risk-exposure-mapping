
import geopandas as gpd
import rasterio
from rasterio.mask import mask
from rasterio.warp import reproject, Resampling
from rasterio.features import geometry_mask
from rasterio.plot import plotting_extent

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

from affine import Affine
import gc

BASE = "/content/drive/MyDrive/Climate_risk_mapping"
