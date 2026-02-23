
flood_data[flood_data == flood_src.nodata] = 0

print("Flood statistics:")
print("Min:", flood_data.min())
print("Max:", flood_data.max())
print("Mean:", flood_data.mean())
print("Pixels > 0:", np.sum(flood_data > 0))
print("% flooded:", 100 * np.sum(flood_data > 0) / flood_data.size)
