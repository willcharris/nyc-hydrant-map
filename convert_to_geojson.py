import geopandas as gpd

gdf = gpd.read_parquet('data/raw/hydrant_density.parquet')
print("geometry column:", gdf.geometry.name)
print("original CRS:", gdf.crs)

gdf = gdf.to_crs(epsg=4326)
print("reprojected CRS:", gdf.crs)

gdf.to_file('data/raw/hydrant_density.geojson', driver='GeoJSON')
print("wrote", len(gdf), "features")
