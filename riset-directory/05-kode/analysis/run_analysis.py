import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# 1. Load Data
df = pd.read_csv('../06-output/tables/full_runs_log.csv')

# 2. Statistik Deskriptif
summary = df.groupby('model')['accuracy'].agg(['mean', 'std', 'median', 'min', 'max'])
summary.to_csv('../06-output/tables/summary_statistics.csv')
print("Statistik Deskriptif:\n", summary)

# 3. Uji Wilcoxon (Statistik Inferensial)
vgg = df[df['model'] == 'VGG-19']['accuracy']
dense = df[df['model'] == 'DenseNet-169']['accuracy']
stat, p_value = stats.wilcoxon(vgg, dense)
print(f"\nHasil Wilcoxon Test: p-value = {p_value}")

# 4. Visualisasi (Boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='model', y='accuracy', data=df)
plt.title('Perbandingan Distribusi Akurasi VGG-19 vs DenseNet-169')
plt.savefig('../06-output/figures/fig_distribution_boxplot.png')
plt.show()