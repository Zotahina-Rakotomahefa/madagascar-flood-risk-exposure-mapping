# Climate Risk Mapping: Flood Exposure Assessment in Madagascar

This project assesses **population exposure to 100-year return period flood hazards (RP100)** in Madagascar using geospatial analysis. It integrates flood hazard rasters, population density data, and administrative boundaries to produce quantitative indicators and high-quality maps supporting climate risk and disaster impact studies.

---

##  Overview

Flooding is one of the most critical climate-related hazards affecting Madagascar. Understanding where people are exposed is essential for disaster risk reduction, climate adaptation planning, and policy decision-making.

This project implements a reproducible Python-based GIS workflow to:

- Align heterogeneous raster datasets
- Quantify exposed population
- Visualize flood risk spatially at national scale

The workflow is optimized for scientific transparency, modularity, and scalability.

---

## Objectives

- Clip flood hazard and population rasters to Madagascar boundaries
- Harmonize spatial resolution, CRS, and extent
- Estimate the total population exposed to RP100 flood events
- Produce a publication-ready flood exposure map
- Provide a modular and reusable Python workflow

---

## Project structure
```
project/
├── data/
     ├── boundaries/                      # Administrative boundaries
     ├── flood/                           # Flood hazard raster
     └── population/                      # Population raster
├── outputs/
     madagascar_flood_map.png        
├── notebooks/
    ├── run_flood_exposure.ipynb          
├── src/ 
    ├── import_config.py                  # Paths, CRS, constants
    ├── input_data.py                     # Data loading
    ├── spatial_clipping.py               # Clip rasters to Madagascar  
    ├── flood_hazard_analysis.py          # Flood mask & statistics
    ├── population_resampling_to_flood_grid.py     
    ├── exposed_population.py             # Exposure calculation
    ├── downscaling.py                    # Resolution harmonization
    ├── population_classification.py      # Population quantile classes
    └── map_production.py                 # Final cartographic output
├── requirements.txt
└── README.md
```

## Installation
```bash
pip install -r requirements.txt
```
---

## Data Sources

Due to file size limitations, datasets are not included in this repository.

### Flood Hazard Data
Source:
https://www.globalflooddata.org

### Population Data
Source: Gridded Population of the World (GPW v4) 
https://sedac.ciesin.columbia.edu/data/collection/gpw-v4

### Administrative Boundaries
Source: GADM - Madagascar boundaries
https://gadm.org  

---

##  Methodology

### Spatial masking

Flood and population rasters are clipped using Madagascar national boundaries.

### Raster harmonization

Population data are reprojected and resampled to match flood raster resolution.

### Flood exposure estimation

A binary flood mask (RP100 > 0) is applied to population data.

### Downscaling for visualization

Raster resolution is reduced for cartographic clarity and performance.

### Classification & mapping

Population values are classified using quantiles and visualized with custom colormaps.

---

##  Key Output

- Total population exposed to RP100 flood hazard
- Spatial distribution of exposed population
- High-resolution PNG map suitable for reports and publications

Example output:
madagascar_flood_map.png

---

##  Scientific Relevance

This workflow can support:

- Climate risk and vulnerability assessment
- Disaster Risk Reduction (DRR) studies
- Habitat suitability studies
- Socio-environmental impact analysis
- Climate adaptation and spatial planning

The methodology aligns with best practices in geospatial climate analysis and can be extended to:
- Other hazards (cyclones, droughts)
- Future climate projections
- Sub-national or district-level analysis
---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software for academic, research, or commercial purposes, provided that proper attribution is given to the original author.

See the `LICENSE` file for full details
