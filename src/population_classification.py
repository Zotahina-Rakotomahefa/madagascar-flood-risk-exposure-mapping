
pop_plot = np.where(pop_plot > 0, pop_plot, np.nan)

bins = np.nanquantile(pop_plot, [0, .4, .7, .9, .97, 1])

colors = ["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"]
labels = [
    "Very low population count",
    "Low population count",
    "Moderate population count",
    "High population count",
    "Very high population count"
]

cmap_pop = ListedColormap(colors)
norm_pop = BoundaryNorm(bins, cmap_pop.N)
