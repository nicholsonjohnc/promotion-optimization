import pandas as pd
import folium

county_data = pd.read_csv('./src/county_data.csv')
county_data['fips'] = county_data['fips'].astype(str)

m = folium.Map(location=[41.95, -93.5], zoom_start=7)

m.choropleth(
    geo_data=r'./src/county_geo.json',
    data=county_data,
    columns=['fips', 'county_consumption'],
    key_on='feature.id',
    fill_color='PuBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Sales (Millions of Liters)',
)
m.save('./img/liquor_sales_choropleth_map.html')





# import pandas as pd
# import folium

# unemployment = pd.read_csv('./src/US_Unemployment_Oct2012.csv')

# m = folium.Map([43,-100], zoom_start=4)

# m.choropleth(
#     geo_data=r'./src/us-states.json',
#     data=unemployment,
#     columns=['State', 'Unemployment'],
#     key_on='feature.id',
#     fill_color='YlGn',
#     )
# m.save('./img/liquor_sales_choropleth_map.html')
