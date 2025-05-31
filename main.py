import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('sp500_fundamentals.csv')

data = data.dropna()
X = data[['Price/Earnings', 'Dividend Yield', 'Market Cap']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_

sns.pairplot(data, hue='Cluster', vars=['Price/Earnings', 'Dividend Yield', 'Market Cap'])
plt.show()

print(data.groupby('Cluster')[['Price/Earnings', 'Dividend Yield', 'Market Cap']].mean())