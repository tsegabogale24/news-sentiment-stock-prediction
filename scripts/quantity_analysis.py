import yfinance as yf
import pandas as pd
import talib
import matplotlib.pyplot as plt

class QuantitativeAnalysis:
    def __init__(self, ticker: str, period: str = "6mo"):
        self.ticker = ticker
        self.period = period
        self.df = pd.DataFrame()
        self.yf_ticker = yf.Ticker(ticker)

    def load_data(self):
        self.df = yf.download(self.ticker, period=self.period)[['Open', 'High', 'Low', 'Close', 'Volume']]
        self.df.dropna(inplace=True)
        print(f"Data loaded for {self.ticker}")
        return self.df

    def compute_indicators(self):
        if self.df.empty:
            raise ValueError("Data not loaded. Call load_data() first.")

        close = self.df['Close'].astype(float).to_numpy().flatten()

        if pd.isnull(close).any():
            raise ValueError("Close prices contain NaN values. Please clean the data.")

        self.df['SMA_20'] = talib.SMA(close, timeperiod=20)
        self.df['RSI'] = talib.RSI(close, timeperiod=14)
        macd, macd_signal, macd_hist = talib.MACD(close)
        self.df['MACD'] = macd
        self.df['MACD_signal'] = macd_signal
        self.df['MACD_hist'] = macd_hist

        print("Indicators computed: SMA_20, RSI, MACD")
#use yfinanace instead of pynance because pynance's API has changed
    def financial_metrics(self):
        print(f"--- Financial Metrics for {self.ticker.upper()} ---")
        try:
            # Get data using yfinance instead since pynance API has changed
            info = self.yf_ticker.info
            
            print("Current Price:      ", info.get('currentPrice', 'N/A'))
            print("P/E Ratio:          ", info.get('trailingPE', 'N/A'))
            print("Earnings Per Share: ", info.get('trailingEps', 'N/A'))
            print("Market Cap:         ", info.get('marketCap', 'N/A'))
            print("52 Week High:       ", info.get('fiftyTwoWeekHigh', 'N/A'))
            print("52 Week Low:        ", info.get('fiftyTwoWeekLow', 'N/A'))
            print("Dividend Yield:     ", info.get('dividendYield', 'N/A'))

        except Exception as e:
            print("Error fetching metrics:", e)

    def visualize(self):
        if self.df.empty:
            raise ValueError("Data not loaded or indicators not computed.")

        plt.figure(figsize=(14, 6))

        # Price and 20-Day Simple Moving Average
        plt.subplot(2, 1, 1)
        plt.plot(self.df['Close'], label='Close Price')
        plt.plot(self.df['SMA_20'], label='SMA 20', linestyle='--')
        plt.title(f'{self.ticker} Price and 20-Day SMA')
        plt.legend()

        # RSI
        plt.subplot(2, 2, 3)
        plt.plot(self.df['RSI'], label='RSI', color='orange')
        plt.axhline(70, linestyle='--', color='red')     # Overbought line
        plt.axhline(30, linestyle='--', color='green')   # Oversold line
        plt.title('RSI')
        plt.legend()

        # MACD
        plt.subplot(2, 2, 4)
        plt.plot(self.df['MACD'], label='MACD')
        plt.plot(self.df['MACD_signal'], label='Signal Line', linestyle='--')
        plt.bar(self.df.index, self.df['MACD_hist'], label='Histogram', alpha=0.3)
        plt.title('MACD')
        plt.legend()

        # Optimize layout and display
        plt.tight_layout()
        plt.show()
