###Contents:
task1_eda.ipynb:
This notebook performs Exploratory Data Analysis (EDA) by importing and using the modular EDA class from scripts/eda_task1.py , Quantity_analysis by importing and using modular QuanitativeAnalysis class and correlation_analysis by importing the modular  Task3SentimentCorrelation

Usage:

###1 from scripts.eda_task1 import EDA

eda = EDA(news_df)
eda.basic_summary()
eda.descriptive_stats()
eda.text_analysis()
eda.time_series_analysis()
eda.publisher_analysis()

###2 from quantity_analysis import QuantitativeAnalysis

qa = QuantitativeAnalysis("AAPL")
qa.load_data()
qa.compute_indicators()
qa.financial_metrics()
qa.visualize()

###3 rom correlation_analysis import Task3SentimentCorrelation

news_df = pd.read_csv("../data/cleaned_news.csv")  
correlation_tool = Task3SentimentCorrelation(news_df, stock_csv_path="../data/META_stock_data.csv")
correlation_tool.align_dates()
correlation_tool.analyze_sentiment()
correlation_tool.aggregate_daily_sentiment()
correlation_tool.calculate_daily_returns()
merged_df, corr, pval = correlation_tool.correlate_sentiment_with_returns()
correlation_tool.plot_correlation_heatmap(merged_df)