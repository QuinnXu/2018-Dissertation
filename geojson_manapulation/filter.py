import json
import csv
import geojson
import pandas as pd

df = pd.read_csv('Nottingham_Data.csv')
lsoacode = list(df['LSOA code (2011)'])

def select(filename):
    f = open(filename,'rb')
    data = json.loads(f.read())
    locations = data['features']
    features = []
    for location in locations:
        if location['properties']['LSOA11CD'] in lsoacode:
            features.append(location)

    new_geojson(features)

def new_geojson(features):
    geofile = {
    "type": "FeatureCollection",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
    "features":features}
    with open ('Nottingham.geojson', 'w') as f:
        json.dump(geofile,f,sort_keys=True,indent=4)
        print('finishing writing')

file = 'lsoa.json'
select(file)


