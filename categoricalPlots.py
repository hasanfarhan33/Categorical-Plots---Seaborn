import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme()

tips = sns.load_dataset('tips')

# Bar plot
# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# Count plot
# sns.countplot(x='sex', data=tips)

# Box plot
# sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

# Violin Plot
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# Strip Plot
# sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# Swarm Plot
# sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex')

# Factor Plot
sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')

plt.show()