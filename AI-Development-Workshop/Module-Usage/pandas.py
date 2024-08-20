# Pandas helps organize data in tables, just like an Excel spreadsheet.

import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [12, 13]}
df = pd.DataFrame(data)
print(df)