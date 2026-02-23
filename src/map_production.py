
fig, ax = plt.subplots(figsize=(12,10))
ax.set_facecolor("#cce6ff")

ax.imshow(
    pop_plot,
    cmap=cmap_pop,
    norm=norm_pop,
    extent=plotting_extent(pop_plot, scaled_transform),
    origin="upper"
)

ax.imshow(
    np.where(flood_plot > 0, 1, np.nan),
    cmap=ListedColormap(["#b30000"]),
    alpha=0.75,
    extent=plotting_extent(flood_plot, scaled_transform),
    origin="upper"
)

madagascar.boundary.plot(ax=ax, edgecolor="black", linewidth=1)

legend_elements = [Patch(facecolor=colors[i], label=labels[i]) for i in range(5)]
legend_elements.append(Patch(facecolor="#b30000", label="Flood hazard extent"))

ax.legend(
    handles=legend_elements,
    title="Population distribution and flood hazard",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5)
)

ax.set_title(
    "Spatial distribution of population and 100-year flood hazard in Madagascar",
    fontsize=14,
    weight="bold"
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

plt.savefig(
    f"{BASE}/outputs/madagascar_flood_map.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
