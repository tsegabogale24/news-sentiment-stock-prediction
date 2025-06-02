Contents:
##1 eda_task1.py:
Contains the modular EDA class to perform four major types of analysis.

Main Functions:
descriptive_stats():
Basic stats like shape, missing values, text length, top publishers, and common words.

text_analysis():
NLP-based text analysis using:
TF-IDF for keyword extraction.
LDA for topic modeling.

time_series_analysis():
Visualizes how article publication frequency changes over time, including spikes or patterns.

publisher_analysis():
Analyzes distribution of articles across different publishers and unique domains.

##2 quantity_analysis.py:

Quantitative Stock Analysis Module
This script provides a streamlined way to perform quantitative technical analysis on any stock ticker using Yahoo Finance data. It calculates key technical indicators, retrieves financial metrics, and visualizes trends—all in one modular class.

  Features
 Download historical price data from Yahoo Finance

 Compute technical indicators:

Simple Moving Average (SMA-20)

Relative Strength Index (RSI)

MACD (Moving Average Convergence Divergence)

 Fetch fundamental financial metrics (P/E ratio, EPS, Market Cap, etc.)

Visualize closing prices, RSI, and MACD with annotated plots
 Dependencies
Make sure to install the required libraries:


pip install yfinance pandas matplotlib TA-Lib
Note: TA-Lib requires native C dependencies. If installation fails, follow platform-specific instructions at: https://mrjbq7.github.io/ta-lib/install.html

 Usage

from scripts.quant_analysis import QuantitativeAnalysis

qa = QuantitativeAnalysis(ticker="AAPL", period="6mo")
qa.load_data()
qa.compute_indicators()
qa.financial_metrics()
qa.visualize()


Output
Technical Indicators Table: A DataFrame with SMA_20, RSI, MACD, MACD_signal, MACD_hist

Financial Metrics: Displayed in console (P/E, EPS, Market Cap, etc.)

Visualizations:

Top: Price chart with 20-day SMA

Bottom left: RSI plot with overbought/oversold lines

Bottom right: MACD with signal and histogram


###3 correlational_analysis

It performs full preprocessing, sentiment analysis using TextBlob, calculates daily returns, and computes the Pearson correlation between sentiment scores and stock movement.

 Features
Cleans and aligns news and stock datasets by date

Performs sentiment analysis on news headlines using TextBlob

Calculates daily stock returns from close prices

Computes Pearson correlation between sentiment and returns

Visualizes the correlation matrix as a heatmap

Dependencies

pip install pandas textblob seaborn matplotlib scipy
 Usage

from scripts.task3_sentiment_correlation import Task3SentimentCorrelation

# Initialize
analyzer = Task3SentimentCorrelation(news_df, stock_csv_path="data/stock_data.csv")

# Run Full Pipeline
merged_df, correlation, p_value = analyzer.run_full_analysis()

# Plot Correlation Heatmap
analyzer.plot_correlation_heatmap(merged_df)
 Output
Pearson correlation coefficient and p-value

Number of overlapping trading days with sentiment and return

 Correlation heatmap of sentiment vs return
