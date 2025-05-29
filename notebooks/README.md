###Contents:
task1_eda.ipynb:
This notebook performs Exploratory Data Analysis (EDA) by importing and using the modular EDA class from scripts/eda_task1.py.

Usage:

from scripts.eda_task1 import EDA

eda = EDA(news_df)
eda.basic_summary()
eda.descriptive_stats()
eda.text_analysis()
eda.time_series_analysis()
eda.publisher_analysis()