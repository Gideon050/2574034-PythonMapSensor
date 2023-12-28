# 2574034-PythonMapSensor
This Python script utilizes various libraries such as Pandas, Matplotlib, Geopandas, and Shapely to process and visualize geographical sensor data stored in a CSV file named 'GrowLocations.csv'. The script performs data cleaning, filtering, visualization, and geospatial manipulation on sensor location coordinates.

Data Loading and Filtering:
Loads the CSV data into a Pandas DataFrame.
Swaps Latitude and Longitude columns and removes rows with zero values in these columns.
Removes duplicate entries based on a unique 'Serial' identifier.
Identifies and isolates rows with latitude and longitude values falling outside specified geographical boundaries.

Visualization:
Plots the cleaned sensor locations on a map image using Matplotlib.
The map image is loaded separately ('map7.png') and used as a background for the scatter plot.

Geospatial Data Handling:
Creates a GeoDataFrame using Geopandas, associating latitude and longitude data with geometric points.
Utilizes Shapely to create Point objects from latitude and longitude coordinates.

Data Output:
Saves information about identified 'bad' values (outside specified boundaries) into a 'bad_values.csv' file.
Saves the cleaned data into two separate files: 'cleaned_data.csv' containing structured data and 'cleaned_data.geojson' in GeoJSON format with associated geospatial information.

This script serves as a comprehensive tool for processing geographical sensor data, cleaning outliers, visualizing sensor locations on a map, and storing cleaned and structured data in different file formats for further analysis or applications.
