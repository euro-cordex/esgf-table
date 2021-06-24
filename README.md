# ESGF Table

[![example workflow](https://github.com/euro-cordex/esgf-crawler/actions/workflows/manual.yml/badge.svg)](https://github.com/euro-cordex/esgf-crawler/actions)

A table of Cordex Simulations currently available in the ESGF. This table is now updated
nightly. The tables contains all Cordex simulation on the `EUR-11` domain.

You can convert this table into a more convenient (humand readable) format using, e.g.

```python
import pandas as pd

url = "https://raw.githubusercontent.com/euro-cordex/esgf-table/master/euro-cordex-esgf.csv"
df = pd.read_csv(url)

# group the data to have a more readable layout.
cordex_table = df.groupby(['institute', 'model_id', 'driving_model_id', 
                           'experiment_id', 'member', 'frequency', 
                           'domain'])['variable'].apply(list).to_frame()

# write the table to excel
cordex_table.to_excel('cordex.xlsx')
```

A formatted table in [`xlsx`](https://raw.githubusercontent.com/euro-cordex/esgf-table/master/euro-cordex-esgf.xlsx) format is also updated nightly.
