
import pandas as pd

url = "https://raw.githubusercontent.com/euro-cordex/tables/master/esgf/euro-cordex-esgf.csv"
df = pd.read_csv(url)

# group the data to have a more readable layout.
cordex_table = df.groupby(['institute', 'model_id', 'driving_model_id', 'experiment_id', 'member', 'frequency', 'date', 'host', 'domain'])['variable'].apply(list).to_frame()

# write the table to excel
cordex_table.to_excel('euro-cordex-esgf.xlsx')
