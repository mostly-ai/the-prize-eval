import json
import os
import pandas as pd

input_dir = 'flat/stage1'
output_dir = 'flat/stage2'

mappings = json.load(open('flat/stage2/mappings.json'))

for fname in os.listdir(input_dir):
    if fname.endswith('.csv.gz'):
        in_path = os.path.join(input_dir, fname)
        out_path = os.path.join(output_dir, fname)
        df = pd.read_csv(in_path)
        df_mapped = df.replace(mappings)
        df_mapped.to_csv(out_path, index=False)
