import yaml
import os
import requests

# Load the YAML file
with open('params.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Get the year and file names
year = data['year']
file_names = data['n_locs']

# Create a data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Download the files
for file_name in file_names:
    url = f'https://www.ncei.noaa.gov/data/local-climatological-data/access/{year}/{file_name}'
    response = requests.get(url)
    
    # Save the file
    with open(f'data/{file_name}', 'wb') as file:
        file.write(response.content)

print("Files downloaded successfully!")
