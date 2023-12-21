import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import _pyio

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('GrowLocations.csv')

# Create filtered_data with swapped Latitude and Longitude columns
filtered_data = data.copy()
filtered_data['Longitude'], filtered_data['Latitude'] = data['Latitude'], data['Longitude']

# Remove rows with zero values in longitude and latitude columns
filtered_data = filtered_data[(filtered_data['Longitude'] != 0) & (filtered_data['Latitude'] != 0)]

# Create a new DataFrame without duplicates
data_no_duplicates = filtered_data.drop_duplicates(subset=['Serial'])

# Remove bad values from dataframe
bad_values = (
    (data_no_duplicates['Longitude'] < -19) | (data_no_duplicates['Longitude'] > 55) |
    (data_no_duplicates['Latitude'] < -18) | (data_no_duplicates['Latitude'] > 59)
)
bad_data = data_no_duplicates[bad_values]

# Remove rows with bad values
clean_data = data_no_duplicates[~bad_values]

# Extract latitude and longitude columns from the dataframe
latitude = clean_data['Latitude']
longitude = clean_data['Longitude']

# Load the map as a background image
map_img = plt.imread('map7.png')

# Create a scatter plot with the sensor locations on the map image
plt.figure(figsize=(10, 8)) # Set the size of the plot
plt.scatter(longitude, latitude, zorder=1, alpha=0.7, c='b', s=10)
plt.imshow(map_img, extent=[-10.592, 1.6848, 50.681, 57.985], zorder=0, aspect='auto')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Sensor Locations on Map')
plt.show()

# Create a GeoDataFrame from latitude and longitude in clean data
geometry = [Point(xy) for xy in zip(clean_data['Latitude'], clean_data['Longitude'])]
geo_data = gpd.GeoDataFrame(clean_data, geometry=geometry, crs='EPSG:4326')

# Save information about bad values to a CSV file
bad_data.to_csv('bad_values.csv', index=False)

# Save cleaned data to a CSV file
clean_data.to_csv('cleaned_data.csv', index=False)

# Save cleaned data to a JSON file
geo_data.to_file('cleaned_data.geojson', driver='GeoJSON')