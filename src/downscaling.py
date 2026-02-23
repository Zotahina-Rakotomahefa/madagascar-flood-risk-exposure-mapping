
scale = 4

new_shape = (
    flood_data.shape[0] // scale,
    flood_data.shape[1] // scale
)

pop_plot   = np.zeros(new_shape, dtype="float32")
flood_plot = np.zeros(new_shape, dtype="uint8")

reproject(
    source=pop_resampled,
    destination=pop_plot,
    src_transform=flood_transform,
    src_crs=flood_src.crs,
    dst_transform=flood_transform * flood_transform.scale(scale, scale),
    dst_crs=flood_src.crs,
    resampling=Resampling.average
)

reproject(
    source=flood_data,
    destination=flood_plot,
    src_transform=flood_transform,
    src_crs=flood_src.crs,
    dst_transform=flood_transform * flood_transform.scale(scale, scale),
    dst_crs=flood_src.crs,
    resampling=Resampling.max
)

scaled_transform = flood_transform * Affine.scale(scale, scale)

del pop_resampled, flood_data
gc.collect()
