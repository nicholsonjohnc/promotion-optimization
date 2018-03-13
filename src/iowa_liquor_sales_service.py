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
    
    
if __name__=='__main__':
    # Call get_top_ten_stores_by_transaction_count example.
    iowa_liquor_sales_service = IowaLiquorSalesService()
    top_ten_stores = iowa_liquor_sales_service.get_top_stores(10)
    print(top_ten_stores.to_csv(columns=['store','name','transactions']))
    # print('store\ttransactions\tname')
    # for store in top_ten_stores:
    #     print('%(store)s\t%(transactions)s\t\t%(name)s' % store)
        
    
        
    