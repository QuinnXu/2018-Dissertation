import json
import pandas as pd

df = pd.read_csv('Nottingham_Data.csv')
lsoacode = list(df['LSOA code (2011)'])
properties = ['Income Score','Education, Skills and Training Score','Health Deprivation and Disability Score','Crime Score','Living Environment Score ']


f = open('Nottingham.json','rb')
Nottingham = json.loads(f.read())

for item in Nottingham['features']:
    for property in properties:
        item['properties'][property] = int(df.loc[(df['LSOA code (2011)'] == item['properties']['LSOA11CD'])][property])

with open('Nottinghamdata.geojson', 'w') as f:
    json.dump(Nottingham, f, sort_keys=True, indent=4)
#income = float(df.loc[(df['LSOA code (2011)'] == 'E01013893')]['Income Score'])

