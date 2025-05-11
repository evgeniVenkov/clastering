
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

# Пример данных
df = pd.DataFrame({
    'feature1': [1, 2, 1, 2, 1, 2],
    'feature2': [3, 4, 5, 6, 7, 8],
    'feature3': [9, 10, 11, 12, 13, 14]
})

# Строим pairplot с hue по 'feature1'
sns.pairplot(df, hue='feature1', palette='Set2')
plt.show()
