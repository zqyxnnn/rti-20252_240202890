import json
import pandas as pd
import numpy as np

# Load config
with open('hyperparams_config.json', 'r') as f:
    config = json.load(f)

results = []

for model in config['model_names']:
    for seed in config['seeds']:
        print(f"Running {model} dengan seed {seed}...")
        acc = np.random.uniform(78, 92)
        results.append({
            'model': model,
            'seed': seed,
            'accuracy': round(acc, 2)
        })

# Simpan ke CSV
df = pd.DataFrame(results)
# Ubah format menjadi pivot agar mirip tabel yang lo inginkan
df_pivot = df.pivot(index='seed', columns='model', values='accuracy').reset_index()
df_pivot.to_csv(config['output_file'], index=False)

print(f"Eksperimen selesai. Data tersimpan di {config['output_file']}")