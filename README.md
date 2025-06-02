# 📊 Cluster Stocks Based on Performance Metrics

This project uses unsupervised learning techniques to group stocks based on their performance metrics. It demonstrates how to apply clustering (specifically K-Means) to financial data, enabling the identification of similar stocks based on key features.

## 🚀 Features

* **Data Loading**: Reads stock data from a CSV file.
* **Feature Extraction**: Selects relevant metrics (e.g., Open, High, Low, Close, Volume) for clustering.
* **Clustering**: Implements K-Means clustering to group stocks based on similarities.
* **Visualization**: Displays clustered stocks in a 2D scatter plot.

## 🛠️ Technologies Used

* Python
* pandas
* scikit-learn (KMeans)
* matplotlib

## 📈 How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/OrasanuAna/Cluster_Stocks_Based_on_Performance_Metrics.git
   cd Cluster_Stocks_Based_on_Performance_Metrics
   ```

2. **Install Dependencies**:
   Make sure you have the required libraries:

   ```bash
   pip install pandas scikit-learn matplotlib
   ```

3. **Prepare the Data**:
   Ensure the `stocks_data.csv` file is present and contains relevant columns (e.g., Date, Open, High, Low, Close, Volume).

4. **Run the Script**:
   Execute the script:

   ```bash
   python main.py
   ```

   The script will:

   * Load and preprocess the data.
   * Perform K-Means clustering.
   * Display a 2D scatter plot showing stock clusters.

## 📊 Sample Output

![Clustering Output](https://github.com/OrasanuAna/Cluster_Stocks_Based_on_Performance_Metrics/blob/master/Problema3%20-%20Cluster%20Stocks%20Based%20on%20Performance%20Metrics.jpg)

*Figure: Clusters of stocks based on selected performance metrics.*
