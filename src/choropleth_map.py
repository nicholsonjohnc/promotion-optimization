import json
import os
import pandas as pd
import folium
# map_osm = folium.Map(location=[45.5236, -122.6750])
# map_osm.save('./img/choropleth_map.html')

rootpath = os.path.abspath(os.path.dirname(__file__))

def setup_data():
    """Import economic data for testing."""
    with open(os.path.join(rootpath, 'iowa-counties.json')) as f:
        get_id = json.load(f)

    county_codes = [x['id'] for x in get_id['features']]
    county_df = pd.DataFrame({'FIPS_Code': county_codes}, dtype=str)

    # Read into Dataframe, cast to string for consistency.
    df = pd.read_csv(os.path.join(rootpath, 'county_data.csv'),
                     na_values=[' '])
    df['FIPS_Code'] = df['FIPS_Code'].astype(str)

    # Perform an inner join, pad NA's with data from nearest county.
    merged = pd.merge(df, county_df, on='FIPS_Code', how='inner')
    return merged.fillna(method='pad')
    
import folium
import pandas as pd

iowa_counties_geo = os.path.join(rootpath, 'iowa_counties.json')
iowa_county_data = os.path.join(rootpath, 'iowa_county_data.csv')

state_data = pd.read_csv(iowa_county_data)

#Let Folium determine the scale
map = folium.Map(location=[48, -102], zoom_start=3)
map.choropleth(geo_path=iowa_counties_geo, data=state_data,
             columns=['County', 'Consumption'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Consumption (Liters)')
map.save('./img/choropleth_map.html')

# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['State', 'Unemployment'],
#     key_on='feature.id',
#     fill_color='YlGn',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name='Unemployment Rate (%)'
# )


