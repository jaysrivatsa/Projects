# Battle of Neighbourhoods
The aim of the project is to identify most popular tourist places in Toronto, Canada and cluster neighbourhoods with similar attraction as clusters. This is done to enable a traveller to selectively visit neighbourhoods of their interest.
## Libraries used
1. Pandas - Used to read and manipulate dataframes.
2. Beautiful Soup - Used for web parsing
3. Numpy - Used for mathematical operations
4. Request - to vist the webpages and to get .json file from the FourSquare API.

## Steps
1. Parse the URL mentioned in the Jupyter notebook for data on Canada's Postal codes.
2. Convert raw data obtained into a  pandas DataFrame
3. Use the 'Geospatial_Coordinates.csv' to get eh co-ordinates for the respective postal codes.
4. Filter the postal codes where the postal code is Toronto.
5. Use FourSquare API to get most popular venues in Toronto in a .json file.
6. Cluster the venues into groups.
