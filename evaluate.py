import os
import pandas as pd
from sklearn.metrics import r2_score

# Load the data
data_dir = 'data'
gt_dir = 'ground_truth'
file_names = os.listdir(data_dir)

results = {}

for file_name in file_names:
    base_name, _ = os.path.splitext(file_name)

    # Load the Ground Truth Data
    df_ground_truth = pd.read_csv(os.path.join(gt_dir, f'monthly_{base_name}.csv'), low_memory=False)

    # Load the Computed Averages Data
    df_computed_avg = pd.read_csv(os.path.join(gt_dir, f'computed_avg_{base_name}.csv'), low_memory=False)

    print(df_ground_truth.shape, df_computed_avg.shape)
    print(df_computed_avg.columns, df_ground_truth.columns)

    # Compute the R2 score
    for i in df_computed_avg.columns:
        if i in df_ground_truth.columns:
            r2 = r2_score(df_ground_truth[i], df_computed_avg[i])
            results[i] = [r2, r2>0.9]

# Store the results in a txt file
with open(os.path.join(gt_dir, 'results.txt'), 'w') as file:
    file.write(str(results))
