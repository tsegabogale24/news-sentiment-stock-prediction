 News Sentiment Stock Prediction
Analyze financial news to predict stock movements using topic modeling, time series analysis, and more.

Project Structure Overview

news-sentiment-stock-prediction/
│
├── notebooks/
├── scripts/
├── tests/
├── .github/
├── .vscode/ 
├── requirements.txt
└── README.md
Setup Instructions
Clone the repository:

 git clone https://github.com/tsegabogale24/news-sentiment-stock-prediction.git
cd news-sentiment-stock-prediction
Create a virtual environment:

python -m venv .venv
# Windows: .venv\Scripts\activate
Install dependencies:
pip install dependencies(pandas , numpy ...)
pip freeze > requirements.txt
Dataset (FNSPID)
headline, url, publisher, date, stock
Source of news used to model potential impact on related stock price movement.

Git Workflow
Create a new branch per task:
git checkout -b eda_task1

git commit -m "Add topic modeling to EDA class"