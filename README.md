# promotion-optimization
Demand modeling and promotion optimization using Iowa Liquor Sales dataset.

## Research questions

Exploratory data analysis
* Which Iowa counties consume the most liquor by volume?
* Who are the top 10 vendors in Iowa by volume?
* What was the top vendor's top selling liquor by volume?

Statistical hypothesis testing
* Does Iowa City, IA (Hawkeyes) drink more than Ames, IA (Cyclones) per capita? 

Demand modeling
* Predict weekly sales as a function of price, seasonality, etc.

Price optimization
* Optimize price to maximize profit.

## Top 10 Stores by Transaction Count.
|   | store | name                                 | transactions | 
|---|-------|--------------------------------------|--------------| 
| 0 | 2633  | Hy-Vee #3 / BDI / Des Moines         | 105536       | 
| 1 | 2190  | "Central City Liquor, Inc."          | 85243        | 
| 2 | 4829  | Central City 2                       | 83430        | 
| 3 | 2512  | Hy-Vee Wine and Spirits / Iowa City  | 80920        | 
| 4 | 2614  | Hy-Vee #3 Food and Drugstore         | 68722        | 
| 5 | 2515  | Hy-Vee Food Store #1 / Mason City    | 64550        | 
| 6 | 2603  | Hy-Vee Wine and Spirits / Bettendorf | 60492        | 
| 7 | 2616  | Hy-Vee Food and Drug / Clinton       | 59046        | 
| 8 | 2500  | Hy-Vee Food Store #1 / Ames          | 58487        | 
| 9 | 2587  | Hy-Vee Food Store / Johnston         | 56929        | 


## Setting APP_TOKEN Environment Variable
In ~/.bashrc add the following at bottom of file:

export APP_TOKEN='YOUR_APP_TOKEN'

App tokens can be obtained [here](https://dev.socrata.com/foundry/data.iowa.gov/spsw-4jax).

## Getting Iowa precinct level shape file

https://sos.iowa.gov/shapefiles/Statewide%20Precinct%20Layer/

https://upload.wikimedia.org/wikipedia/commons/5/5f/USA_Counties_with_FIPS_and_names.svg



![Alt text](./choropleth_map.svg)
<img src="./img/choropleth_map.svg">

