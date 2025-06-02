import pandas as pd
from textblob import TextBlob
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

class Task3SentimentCorrelation:
    def __init__(self, news_df, stock_csv_path):
        print("[INIT] Initializing Sentiment Correlation Analysis...")

        # Standardize and clean news data
        self.news_df = news_df.copy()
        self.news_df['date'] = pd.to_datetime(self.news_df['date'], errors='coerce').dt.date
        self.news_df = self.news_df[self.news_df['headline'] != ""]
        self.news_df.drop_duplicates(subset=['date', 'headline'], inplace=True)

        # Load and clean stock data
        print(f"[INFO] Loading stock data from {stock_csv_path}...")
        try:
            self.stock_df = pd.read_csv(stock_csv_path)

            # Strip whitespace from column names
            self.stock_df.columns = [col.strip() for col in self.stock_df.columns]

            # Convert 'Date' column
            self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'], errors='coerce')

            # Drop invalid dates
            self.stock_df.dropna(subset=['Date'], inplace=True)

            # Set index
            self.stock_df.set_index('Date', inplace=True)

            # Convert numeric columns
            numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
            for col in numeric_cols:
                if col in self.stock_df.columns:
                    self.stock_df[col] = pd.to_numeric(self.stock_df[col], errors='coerce')

            # Add 'date' column and drop rows without Close
            self.stock_df['date'] = self.stock_df.index.date
            self.stock_df.dropna(subset=['Close'], inplace=True)

            print(f"[INFO] Loaded stock data from {self.stock_df.index.min()} to {self.stock_df.index.max()}")

        except Exception as e:
            print(f"[ERROR] Failed to load stock data: {str(e)}")
            raise


    def align_dates(self):
        """Align news dates with available trading days"""
        print("[INFO] Aligning news with stock trading days...")
        trading_days = set(self.stock_df['date'].unique())
        self.news_df = self.news_df[self.news_df['date'].isin(trading_days)]
        print(f"[INFO] {len(self.news_df)} news items aligned with trading days")

    def analyze_sentiment(self):
        """Perform sentiment analysis on headlines"""
        print("[INFO] Performing sentiment analysis on headlines...")
        self.news_df['sentiment'] = self.news_df['headline'].apply(
            lambda text: TextBlob(str(text)).sentiment.polarity
        )
        print("[INFO] Sentiment analysis completed")

    def aggregate_daily_sentiment(self):
        """Calculate average sentiment per day"""
        print("[INFO] Aggregating daily sentiment scores...")
        self.daily_sentiment = self.news_df.groupby('date')['sentiment'].mean().reset_index()
        print(f"[INFO] Aggregated sentiment for {len(self.daily_sentiment)} days")

    def calculate_daily_returns(self):
        """Calculate daily percentage returns"""
        print("[INFO] Calculating daily stock returns...")
        self.stock_df['return'] = self.stock_df['Close'].pct_change() * 100  # Convert to percentage
        self.daily_returns = self.stock_df[['date', 'return']].dropna()
        print(f"[INFO] Returns calculated for {len(self.daily_returns)} trading days")

    def correlate_sentiment_with_returns(self):
        """Calculate correlation between sentiment and returns"""
        print("[INFO] Merging sentiment with returns and computing correlation...")
        
        # Merge sentiment and returns data
        merged_df = pd.merge(self.daily_sentiment, self.daily_returns, on='date')
        
        if len(merged_df) < 2:
            print("[WARNING] Not enough overlapping data points for correlation")
            return None, None, None
            
        # Calculate Pearson correlation
        correlation, p_value = pearsonr(merged_df['sentiment'], merged_df['return'])

        print("\n=== Correlation Results ===")
        print(f"Pearson Correlation: {correlation:.4f}")
        print(f"P-Value: {p_value:.4f}")
        print(f"Number of overlapping days: {len(merged_df)}")
        
        return merged_df, correlation, p_value

    def run_full_analysis(self):
        """Run the complete analysis pipeline"""
        self.align_dates()
        self.analyze_sentiment()
        self.aggregate_daily_sentiment()
        self.calculate_daily_returns()
        return self.correlate_sentiment_with_returns()
   

    def plot_correlation_heatmap(self , df):
      """Plot a heatmap of correlations between sentiment and return"""
      corr_matrix = df[['sentiment', 'return']].corr()
    
      plt.figure(figsize=(6, 4))
      sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
      plt.title("Correlation Heatmap: Sentiment vs Stock Return")
      plt.tight_layout()
      plt.show()
