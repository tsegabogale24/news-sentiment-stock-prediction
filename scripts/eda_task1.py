import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class EDA:
    def __init__(self, df):
        self.df = df.copy()
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')  # parse dates

    def basic_summary(self):
        print(" DataFrame Shape:", self.df.shape)
        print("\n Columns:", list(self.df.columns))
        print("\n Data Types:\n", self.df.dtypes)
        print("\n Missing Values Summary:")
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        print(pd.DataFrame({
            "Missing Values": missing,
            "% of Total": missing_percent
        }).sort_values(by="Missing Values", ascending=False))

        print("\n Descriptive Statistics:\n", self.df.describe(include='all'))

    def descriptive_statistics(self):
        print(" Basic Descriptive Stats\n")
        self.df['headline_length'] = self.df['headline'].astype(str).apply(len)
        print(self.df['headline_length'].describe())

        print("\n Top 10 Most Active Publishers")
        print(self.df['publisher'].value_counts().head(10))

        print("\n Articles Published Over Time")
        articles_per_day = self.df.groupby(self.df['date'].dt.date).size()
        articles_per_day.plot(figsize=(12, 4), title="Articles Published per Day")
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.grid()
        plt.tight_layout()
        plt.show()

    def text_topic_modeling(self, n_topics=5):
        print("🔹 Topic Modeling\n")

        # Simple preprocessing
        headlines = self.df['headline'].dropna().astype(str).tolist()
        vectorizer = CountVectorizer(stop_words='english', max_df=0.9, min_df=2)
        X = vectorizer.fit_transform(headlines)

        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(X)

        words = vectorizer.get_feature_names_out()
        for idx, topic in enumerate(lda.components_):
            print(f"\nTopic #{idx + 1}:")
            print([words[i] for i in topic.argsort()[-10:]])

    def time_series_analysis(self):
        """
        Analyzes publication frequency over time and by hour of day.
        Produces two plots:
            1. Daily news article frequency
            2. Hourly news article distribution
        """
        print("[INFO] Performing time series analysis...")

        # Ensure 'date' is datetime
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df.dropna(subset=['date'], inplace=True)

        # --- Plot 1: Daily frequency ---
        self.df["date_only"] = self.df["date"].dt.date
        daily_counts = self.df.groupby("date_only").size()

        plt.figure(figsize=(14, 5))
        daily_counts.plot()
        plt.title("📅 Daily News Article Frequency")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # --- Plot 2: Hourly distribution ---
        self.df["hour"] = self.df["date"].dt.hour
        hourly_counts = self.df["hour"].value_counts().sort_index()

        plt.figure(figsize=(10, 4))
        hourly_counts.plot(kind="bar", color='teal')
        plt.title("⏰ News Articles by Hour of Day")
        plt.xlabel("Hour (24-hour format)")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=0)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        print("[INFO] Time series analysis completed successfully.")

    def publisher_analysis(self):
        print("🔹 Publisher Analysis\n")
        top_publishers = self.df['publisher'].value_counts().head(10)
        top_publishers.plot(kind='barh', figsize=(8, 5), title="Top 10 Publishers")
        plt.xlabel("Number of Articles")
        plt.ylabel("Publisher")
        plt.grid()
        plt.tight_layout()
        plt.show()
    def get_cleaned_news(self):
       cleaned = self.df.copy()
    # Drop rows with missing or empty headlines or dates
       cleaned = cleaned.dropna(subset=['headline', 'date'])
       cleaned['headline'] = cleaned['headline'].astype(str).str.strip()
       cleaned = cleaned[cleaned['headline'] != ""]
    # Standardize date to date only (not datetime)
       cleaned['date'] = pd.to_datetime(cleaned['date']).dt.date
       cleaned = cleaned.drop_duplicates(subset=['date', 'headline'])
       return cleaned[['date', 'headline']]