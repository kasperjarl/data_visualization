from pathlib import Path
import json

# Read data as a string and convert to a Python object. 
path = Path('../eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earhquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Magnitudes
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
print(mags[:1], lons[:1], lats[:1], eq_titles[:1])

