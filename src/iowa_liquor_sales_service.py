import os
from sodapy import Socrata
import pandas as pd

class IowaLiquorSalesService(object):
    
    def __init__(self):
        self.PREFIX = 'https://'
        self.DOMAIN = 'data.iowa.gov'
        self.DATASET_IDENTIFIER = 'spsw-4jax'
        # Get APP_TOKEN environment variable.
        # See README.md 'Setting APP_TOKEN Environment Variable' for help.
        self.APP_TOKEN = os.environ['APP_TOKEN']
        self.TIMEOUT = 60
        self.CONTENT_TYPE = 'json'
    
    def query(self, query_string):
        '''
        Query Iowa Liquor Sales API.
        '''
        with Socrata(self.DOMAIN, self.APP_TOKEN, timeout=self.TIMEOUT) as client:
            return client.get(self.DATASET_IDENTIFIER, content_type=self.CONTENT_TYPE, query=query_string)
        
    def get_top_stores(self, limit=1):
        '''
        Get top stores by transaction count.
        '''
        return pd.DataFrame.from_dict(self.query('SELECT store, name, COUNT(*) AS transactions GROUP BY store, name ORDER BY transactions DESC LIMIT ' + str(limit)))
        
    def get_top_beverages(self, store, limit=1):
        '''
        Get top beverages by 
        '''
        # return self.query()
        pass
    
    def get_iowa_consumption(self):
        '''
        Get volume (in liters) Iowa consumed as scalar.
        '''
        return self.query('SELECT SUM(sale_liters) as iowa_consumption')[0]['iowa_consumption']
        
    def get_county_consumption(self):
        '''
        Get volume (in liters) each county consumed as pandas dataframe.
        '''
        df = pd.DataFrame.from_dict(self.query('SELECT upper(County) AS county, SUM(sale_liters) as county_consumption GROUP BY county ORDER BY county ASC'))
        df = df.set_index('county')
        df['county_consumption'] = pd.to_numeric(df['county_consumption'], errors='coerce')
        # Combine BUENA VIST into BUENA VISTA and drop BUENA VIST.
        df['county_consumption'].loc['BUENA VISTA'] += df['county_consumption'].loc['BUENA VIST']
        df.drop('BUENA VIST', inplace=True)
        # Combine CERRO GORD into CERRO GORDO and drop CERRO GORD.
        df['county_consumption'].loc['CERRO GORDO'] += df['county_consumption'].loc['CERRO GORD']
        df.drop('CERRO GORD', inplace=True)
        # Combine OBRIEN into O'BRIEN and drop OBRIEN.
        df['county_consumption'].loc["O'BRIEN"] += df['county_consumption'].loc['OBRIEN']
        df.drop('OBRIEN', inplace=True)
        # Combine POTTAWATTA into POTTAWATTAMIE and drop POTTAWATTA.
        df['county_consumption'].loc['POTTAWATTAMIE'] += df['county_consumption'].loc['POTTAWATTA']
        df.drop('POTTAWATTA', inplace=True)
        return df[:-1] # Return all but final row, which is NaN.
        
    def get_top_vendors(self):
        df = pd.DataFrame.from_dict(self.query('SELECT vendor_no AS ID, SUM(sale_dollars) AS Sales GROUP BY ID ORDER BY Sales DESC LIMIT 10')).set_index('ID')
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
        return df
        
    def get_top_liquors(self):
        liquors = pd.DataFrame.from_dict(self.query("SELECT vendor_no AS VendorID, itemno AS ItemID, SUM(sale_dollars) AS Sales WHERE VendorID='65' GROUP BY VendorID, ItemID ORDER BY Sales DESC LIMIT 10"))
        liquors['Sales'] = pd.to_numeric(liquors['Sales'], errors='coerce')
        itemIDs = liquors['ItemID'].values
        itemNames = pd.DataFrame.from_dict(self.query("SELECT itemno AS ItemID, im_desc AS Item, bottle_volume_ml AS Volume WHERE ItemID IN {} GROUP BY ItemID, Item, Volume".format(tuple(itemIDs))))
        return pd.merge(pd.DataFrame(liquors).set_index('ItemID'),pd.DataFrame(itemNames).set_index('ItemID'),left_index=True,right_index=True)
        
    def get_item(self):
        print(self.query("SELECT COUNT(*) WHERE itemno='19068' AND vendor_no='65'"))
        return pd.DataFrame.from_dict(self.query("SELECT itemno, vendor_no, date, invoice_line_no, pack, sale_bottles, sale_dollars, state_bottle_retail WHERE itemno='19068' AND vendor_no='65' ORDER BY date DESC LIMIT 10"))
    
    def get_item_data_agg_by_month(self):
        df = pd.DataFrame.from_dict(self.query("SELECT itemno, vendor_no, date, invoice_line_no, pack, sale_bottles, sale_dollars, state_bottle_retail WHERE itemno='19068' AND vendor_no='65' ORDER BY date ASC LIMIT 50000")).set_index('invoice_line_no')
        return df
    
if __name__=='__main__':
    # # Call get_top_ten_stores_by_transaction_count example.
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # top_ten_stores = iowa_liquor_sales_service.get_top_stores(10)
    # print(top_ten_stores.to_csv(columns=['store','name','transactions']))
    # # print('store\ttransactions\tname')
    # # for store in top_ten_stores:
    # #     print('%(store)s\t%(transactions)s\t\t%(name)s' % store)
        
    # # Get Iowa consumption example.
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # print(iowa_liquor_sales_service.get_iowa_consumption())
    
    # # Get county consumption example.
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # df = iowa_liquor_sales_service.get_county_consumption()
    
    
    # with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
    #     print(df)
    
    # with Socrata(iowa_liquor_sales_service.DOMAIN, iowa_liquor_sales_service.APP_TOKEN, timeout=iowa_liquor_sales_service.TIMEOUT) as client:
    #     print(client.get_metadata(iowa_liquor_sales_service.DATASET_IDENTIFIER, content_type=iowa_liquor_sales_service.CONTENT_TYPE))
    
        
    # # Get top 10 vendors in Iowa by sales.
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # df = iowa_liquor_sales_service.get_top_vendors()
    # df['Sales'] = (df['Sales'] / 1000000).round(2)
    # df.to_csv('top_vendors.csv')
    
    # # Get top 10 liquors by sales.
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # df = iowa_liquor_sales_service.get_top_liquors()
    # df['Sales'] = (df['Sales'] / 1000000).round(2)
    # df.to_csv('top_liquors.csv')
   
    # 
    # iowa_liquor_sales_service = IowaLiquorSalesService()
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(iowa_liquor_sales_service.get_item())
        
        
    iowa_liquor_sales_service = IowaLiquorSalesService()
    iowa_liquor_sales_service.get_item_data_agg_by_month().to_csv('item_sales.csv')