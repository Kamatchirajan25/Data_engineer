import flatten_json
import json

import pandas as pd

#load json object
with open('E:\DATA_WORKS\sample_data.json') as f:
    d = json.load(f)


print(pd.json_normalize(d))


