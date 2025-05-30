import pandas as pd
from scripts.eda_task1 import EDA

def test_descriptive_stats():
    # Create a small DataFrame for testing
    df = pd.DataFrame({
        'headline': ['Stock hits high', 'Earnings beat expectations'],
        'publisher': ['Reuters', 'Bloomberg'],
        'date': ['2024-01-01 10:00:00', '2024-01-02 11:30:00'],
        'stock': ['AAPL', 'GOOG']
    })
    
    eda = EDA(df)
    
    # Just checking if it runs without crashing
    try:
        eda.descriptive_stats()
    except Exception as e:
        assert False, f"descriptive_stats failed with: {e}"
def test_publisher_analysis_type():
    df = pd.DataFrame({
        'headline': ['News A', 'News B'],
        'publisher': ['abc.com', 'xyz.com'],
        'date': ['2024-01-01 09:00:00', '2024-01-01 10:00:00'],
        'stock': ['TSLA', 'MSFT']
    })
    eda = EDA(df)
    result = eda.publisher_analysis()
    assert isinstance(result, pd.Series)
def test_time_series_analysis_runs():
    df = pd.DataFrame({
        'headline': ['News A', 'News B', 'News C'],
        'publisher': ['abc', 'xyz', 'abc'],
        'date': ['2024-01-01 09:00:00', '2024-01-01 10:00:00', '2024-01-02 10:00:00'],
        'stock': ['TSLA', 'AAPL', 'MSFT']
    })
    eda = EDA(df)
    
    try:
        eda.time_series_analysis()
    except Exception as e:
        assert False, f"time_series_analysis failed: {e}"

