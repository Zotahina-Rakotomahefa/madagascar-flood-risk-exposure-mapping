
pop_resampled = np.zeros_like(flood_data, dtype="float32")

reproject(
    source=pop_data,
    destination=pop_resampled,
    src_transform=pop_transform,
    src_crs=pop_src.crs,
    dst_transform=flood_transform,
    dst_crs=flood_src.crs,
    resampling=Resampling.sum
)

pop_resampled[pop_resampled < 0] = 0

del pop_data
gc.collect()
