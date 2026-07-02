# NYC Fire Hydrant Density

An interactive choropleth map of fire hydrant density across New York City neighborhoods.

**Live map:** https://will3ch.github.io/nyc-hydrant-map/

## What this shows

Each polygon is a NYC neighborhood (2020 Neighborhood Tabulation Area). Color indicates hydrant density in hydrants per square kilometer, from under 95/km² (yellow) to over 255/km² (dark blue). Click any neighborhood for its name, borough, hydrant count, and density.

## Data sources

- **[Hydrants](https://data.cityofnewyork.us/Environment/Hydrants/5bgh-vtsn)** — NYC Open Data, dataset `5bgh-vtsn`. 109,725 hydrant point locations citywide.
- **[2020 Neighborhood Tabulation Areas (NTAs)](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd)** — NYC Open Data, dataset `9nt8-h7nd`. 262 neighborhood boundary polygons.

3 of the 262 NTAs have zero hydrants and are excluded from the join-based density calculation, so 259 neighborhoods appear in the final map.

## How it was built

This map is the second half of a two-part project:

1. **[nyc-hydrant-analysis](https://github.com/Will3CH/nyc-hydrant-analysis)** — SQL and Python pipeline using PostGIS and GeoPandas to join hydrant points against NTA boundaries and compute density per neighborhood. Outputs a GeoParquet file.
2. **This repo** — takes that GeoParquet, converts it to GeoJSON with GeoPandas, builds vector tiles with [tippecanoe](https://github.com/felt/tippecanoe), and renders them in the browser with [MapLibre GL JS](https://maplibre.org/) reading directly from a single [PMTiles](https://github.com/protomaps/PMTiles) file — no tile server required. Deployed as a static site on GitHub Pages.

## Stack

- **Data processing:** PostGIS, GeoPandas
- **Tiling:** tippecanoe → PMTiles
- **Rendering:** MapLibre GL JS
- **Hosting:** GitHub Pages (static, $0/month, no server)

## How to run locally

PMTiles requires HTTP range request support, which Python's built-in `http.server` doesn't provide. Use:

```bash
pip install rangehttpserver
python -m RangeHTTPServer 8000
```

Then visit `http://localhost:8000/index.html`.

## License

MIT.
