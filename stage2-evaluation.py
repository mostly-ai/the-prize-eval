#!uv pip install mostlyai-qa==1.9.8

import pandas as pd
import json
import os
from mostlyai import qa
from pathlib import Path

for type in ['flat', 'sequential']:
    for subm_id in range(1, 6):
        for run_id in range(1, 7):

            syn_path = f'../the-prize-eval/{type}/stage2/submissions/synthetic-{type.upper()[:4]}{subm_id}-run{run_id}.csv.gz'
            metrics_path = f'../the-prize-eval/{type}/stage2/submissions/metrics-{type.upper()[:4]}{subm_id}-run{run_id}.json'

            if not os.path.exists(syn_path):
                print(f"Skipping: synthetic file does not exist: {syn_path}")
                continue

            if os.path.exists(metrics_path):
                print(f"Skipping: metrics file already exists: {metrics_path}")
                continue

            qa.set_random_state(run_id)
            qa.init_logging()

            syn = pd.read_csv(syn_path)
            trn = pd.read_csv(f'../the-prize-eval/{type}/stage2/{type}-training.csv.gz')
            hol = pd.read_csv(f'../the-prize-eval/{type}/stage2/{type}-holdout.csv.gz')

            report_path, metrics = qa.report(
                syn_tgt_data=syn,
                trn_tgt_data=trn,
                hol_tgt_data=hol,
                tgt_context_key = "group_id" if type == 'sequential' else None,
            )

            with open(metrics_path, 'w') as f:
                f.write(metrics.model_dump_json(indent=4))

            print(f"Saved metrics to: {metrics_path}")


def flatten_metrics(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    flat = {}
    for section, metrics in data.items():
        for k, v in metrics.items():
            flat[f'{section}_{k}'] = v
    flat['distances_nndr_ratio'] = flat['distances_nndr_training'] / flat['distances_nndr_holdout']
    flat['file'] = file_path.name.replace('metrics', 'synthetic').replace('.json', '.csv.gz') 
    return flat

files = list(Path('.').glob('*/stage2/submissions/*.json'))
metrics = pd.DataFrame([flatten_metrics(f) for f in files])

# merge metrics with results
results = pd.read_csv('stage2-results.csv')
results = results.drop(columns=[c for c in metrics.columns if c != 'file'], errors='ignore')

df = pd.merge(results, metrics, on='file', how='left')
df.to_csv('stage2-results.csv', index=False)
print('saved metrics to results.csv')






# PLOTS #

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_accuracy_by_participant(
    df, 
    task_prefix, 
    title, 
    xlim, 
    grid_start, 
    grid_end, 
    grid_step, 
    filename
):
    # Filter for the given task type
    task_df = df[df['task'].str.startswith(task_prefix)].copy()
    task_df['accuracy_overall'] = pd.to_numeric(task_df['accuracy_overall'], errors='coerce')

    # Find max accuracy per participant
    max_acc = task_df.groupby('participant')['accuracy_overall'].transform('max')
    task_df['is_max'] = task_df['accuracy_overall'] == max_acc

    # Sort participants by their max score (descending)
    max_scores = task_df.groupby('participant')['accuracy_overall'].max().sort_values(ascending=False)
    ordered_participants = list(max_scores.index)

    plt.figure(figsize=(8, 5))

    # Plot all points except max (gray)
    sns.stripplot(
        data=task_df[~task_df['is_max']],
        y='participant',
        x='accuracy_overall',
        color='gray',
        size=8,
        jitter=0.08,
        dodge=False,
        alpha=0.7,
        order=ordered_participants
    )
    # Plot max points (blue) on top
    sns.stripplot(
        data=task_df[task_df['is_max']],
        y='participant',
        x='accuracy_overall',
        color='royalblue',
        size=8,
        jitter=0.08,
        dodge=False,
        alpha=0.9,
        order=ordered_participants
    )

    # Annotate max points, with 4 digits
    for idx, row in task_df[task_df['is_max']].iterrows():
        plt.text(
            row['accuracy_overall'] + 0.00018,
            ordered_participants.index(row['participant']),
            f"{row['accuracy_overall']:.4f}",
            va='center',
            ha='left',
            color='royalblue',
            fontsize=10,
            fontweight='bold'
        )

    plt.xlabel('Overall Accuracy', labelpad=10)
    plt.ylabel('Participant', labelpad=10)
    plt.title(title, pad=12)
    plt.ylim(len(ordered_participants)-0.5, -0.5)  # Reverse y-axis
    plt.xlim(*xlim)

    # Set custom grid lines
    grid_x = np.arange(grid_start, grid_end, grid_step)
    plt.xticks(grid_x)
    plt.grid(axis='x', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
    plt.grid(axis='y', linestyle=':', linewidth=0.5, color='gray', alpha=0.5)

    plt.legend([],[], frameon=False)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f'saved plot to {filename}')

# Load the data
df = pd.read_csv('stage2-results.csv')

# FLAT chart
plot_accuracy_by_participant(
    df,
    task_prefix='FLAT',
    title='The FLAT DATA Challenge',
    xlim=(0.9835, 0.9925),
    grid_start=0.984,
    grid_end=0.993,
    grid_step=0.001,
    filename='flat-final.png'
)

# SEQUENTIAL chart
plot_accuracy_by_participant(
    df,
    task_prefix='SEQU',
    title='The SEQUENTIAL DATA Challenge',
    xlim=(0.961, 0.975),
    grid_start=0.962,
    grid_end=0.975,
    grid_step=0.002,
    filename='sequential-final.png'
)
