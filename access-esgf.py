from cordex import esgf_access

import pandas as pd

# Euro-Cordex search attributes
attrs = {'project':'CORDEX', 'domain':'EUR-11'}

# create a datasets search result object
results = esgf_access.datasets(attrs, verbose=True)

# creates a pandas dataframe from dataset ids
df = esgf_access.to_pandas(results, columns='CORDEX')
print(df)
df.to_csv('euro-cordex-esgf.csv', index=False)

# regroup dataframe for excel output
cordex_list = df.groupby(['institute', 'model_id', 'driving_model_id', 'experiment_id', 
                          'member', 'frequency', 'date', 'host', 'domain'])['variable'].apply(list).to_frame()
print(cordex_list)

cordex_list.to_excel('euro-cordex-esgf.xlsx')
