
madagascar = gpd.read_file(
    f"{BASE}/data/boundaries/madagascar_boundary.shp"
)

flood_src = rasterio.open(
    f"{BASE}/data/flood/flood_madagascar_merged.tif"
)

pop_src = rasterio.open(
    f"{BASE}/data/population/mdg_ppp_2020_UNadj.tif"
)
