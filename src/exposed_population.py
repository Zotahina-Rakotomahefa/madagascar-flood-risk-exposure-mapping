
flood_mask = flood_data > 0
exposed_population = pop_resampled * flood_mask

total_exposed = exposed_population.sum()
print("Population exposed to RP100 flood:", int(total_exposed))
