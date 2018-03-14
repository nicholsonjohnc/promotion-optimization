### color_map.py
 
import csv
from bs4 import BeautifulSoup
from iowa_liquor_sales_service import IowaLiquorSalesService
import pandas as pd
import numpy as np
 

 
# Get county consumption example.
iowa_liquor_sales_service = IowaLiquorSalesService()
df = iowa_liquor_sales_service.get_county_consumption()

df_temp = pd.DataFrame.from_records([('ADAIR', 19001), ('ADAMS', 19003), ('ALLAMAKEE', 19005), ('APPANOOSE', 19007), ('AUDUBON', 19009), ('BENTON', 19011), ('BLACK HAWK', 19013), ('BOONE', 19015), ('BREMER', 19017), ('BUCHANAN', 19019), ('BUENA VISTA', 19021), ('BUTLER', 19023), ('CALHOUN', 19025), ('CARROLL', 19027), ('CASS', 19029), ('CEDAR', 19031), ('CERRO GORDO', 19033), ('CHEROKEE', 19035), ('CHICKASAW', 19037), ('CLARKE', 19039), ('CLAY', 19041), ('CLAYTON', 19043), ('CLINTON', 19045), ('CRAWFORD', 19047), ('DALLAS', 19049), ('DAVIS', 19051), ('DECATUR', 19053), ('DELAWARE', 19055), ('DES MOINES', 19057), ('DICKINSON', 19059), ('DUBUQUE', 19061), ('EMMET', 19063), ('FAYETTE', 19065), ('FLOYD', 19067), ('FRANKLIN', 19069), ('FREMONT', 19071), ('GREENE', 19073), ('GRUNDY', 19075), ('GUTHRIE', 19077), ('HAMILTON', 19079), ('HANCOCK', 19081), ('HARDIN', 19083), ('HARRISON', 19085), ('HENRY', 19087), ('HOWARD', 19089), ('HUMBOLDT', 19091), ('IDA', 19093), ('IOWA', 19095), ('JACKSON', 19097), ('JASPER', 19099), ('JEFFERSON', 19101), ('JOHNSON', 19103), ('JONES', 19105), ('KEOKUK', 19107), ('KOSSUTH', 19109), ('LEE', 19111), ('LINN', 19113), ('LOUISA', 19115), ('LUCAS', 19117), ('LYON', 19119), ('MADISON', 19121), ('MAHASKA', 19123), ('MARION', 19125), ('MARSHALL', 19127), ('MILLS', 19129), ('MITCHELL', 19131), ('MONONA', 19133), ('MONROE', 19135), ('MONTGOMERY', 19137), ('MUSCATINE', 19139), ("O'BRIEN", 19141), ('OSCEOLA', 19143), ('PAGE', 19145), ('PALO ALTO', 19147), ('PLYMOUTH', 19149), ('POCAHONTAS', 19151), ('POLK', 19153), ('POTTAWATTAMIE', 19155), ('POWESHIEK', 19157), ('RINGGOLD', 19159), ('SAC', 19161), ('SCOTT', 19163), ('SHELBY', 19165), ('SIOUX', 19167), ('STORY', 19169), ('TAMA', 19171), ('TAYLOR', 19173), ('UNION', 19175), ('VAN BUREN', 19177), ('WAPELLO', 19179), ('WARREN', 19181), ('WASHINGTON', 19183), ('WAYNE', 19185), ('WEBSTER', 19187), ('WINNEBAGO', 19189), ('WINNESHIEK', 19191), ('WOODBURY', 19193), ('WORTH', 19195), ('WRIGHT', 19197)], columns=['county','fips'])
df_temp = df_temp.set_index('county')

df = pd.merge(pd.DataFrame(df),pd.DataFrame(df_temp),left_index=True,right_index=True)
df = df.set_index('fips')



df['county_consumption'] = df['county_consumption'] / 1000000

df.to_csv('iow_county_data.csv')
# print(df['county_consumption_scaled'].sum())


# with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#     print(df)
 
# Load the SVG map
svg = open('./img/counties.svg', 'r').read()
 
# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
 
# Find counties
paths = soup.findAll('path')
 
# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
 
# County style
path_style = '''font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;
stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;
marker-start:none;stroke-linejoin:bevel;fill:'''
 
# Color the counties based on unemployment rate
print(df)
# print(df['county_consumption_scaled'].loc[19001])
# print(df['county_consumption'].at('19003'))
for p in paths:
    # print(p)
    if p['id'] not in ["State_Lines", "separator"]:
        try:
            # print(p['id'])
            rate = df['county_consumption_scaled'].loc[int(p['id'])]
            # print(rate)
            # rate = unemployment[p['id']]
        except:
            continue
             
         
        if rate > 0.1:
            color_class = 5
        elif rate > 0.01:
            color_class = 4
        elif rate > 0.001:
            color_class = 3
        elif rate > 0.0001:
            color_class = 2
        elif rate > 0.00001:
            color_class = 1
        else:
            color_class = 0
 
 
        color = colors[color_class]
        p['style'] = path_style + color
 

with open("./img/choropleth_map.svg", "w") as svg:
    svg.write(soup.prettify())
