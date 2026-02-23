
geom = madagascar.geometry.values

flood_clip, flood_transform = mask(
    flood_src, geom, crop=True, filled=True
)

pop_clip, pop_transform = mask(
    pop_src, geom, crop=True, filled=True
)

flood_data = flood_clip[0].astype("float32")
pop_data   = pop_clip[0].astype("float32")

del flood_clip, pop_clip
gc.collect()
