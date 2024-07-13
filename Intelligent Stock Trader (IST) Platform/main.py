from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import yfinance as yf
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample data: Replace this with actual stock symbols and company names
stock_data = {
    'AAPL': 'Apple Inc.',
    'GOOGL': 'Alphabet Inc.',
    'MSFT': 'Microsoft Corporation',
    'AMZN': 'Amazon.com Inc.',
    'TSLA': 'Tesla Inc.',
    'FB': 'Meta Platforms Inc.',
    'NVDA': 'NVIDIA Corporation',
    'PYPL': 'PayPal Holdings Inc.',
    'INTC': 'Intel Corporation',
    'CSCO': 'Cisco Systems Inc.',
    'IBM': 'International Business Machines Corporation',
    'QCOM': 'QUALCOMM Incorporated',
    'V': 'Visa Inc.',
    'NFLX': 'Netflix Inc.',
    'DIS': 'The Walt Disney Company',
    'BA': 'The Boeing Company',
    'GS': 'The Goldman Sachs Group Inc.',
    'JPM': 'JPMorgan Chase & Co.',
    'WMT': 'Walmart Inc.',
    'KO': 'The Coca-Cola Company',
    'PEP': 'PepsiCo Inc.',
    'MCD': "McDonald's Corporation",
    'GE': 'General Electric Company',
    'GM': 'General Motors Company',
    'F': 'Ford Motor Company',
    'T': 'AT&T Inc.',
    'GOOG': 'Alphabet Inc. (Class C)',
    'C': 'Citigroup Inc.',
    'XOM': 'Exxon Mobil Corporation',
    'CVX': 'Chevron Corporation',
    'PG': 'Procter & Gamble Company',
    'JNJ': 'Johnson & Johnson',
    'UNH': 'UnitedHealth Group Incorporated',
    'VZ': 'Verizon Communications Inc.',
    'MRK': 'Merck & Co. Inc.',
    'PFE': 'Pfizer Inc.',
    'ABT': 'Abbott Laboratories',
    'GILD': 'Gilead Sciences Inc.',
    'TSM': 'Taiwan Semiconductor Manufacturing Company Limited',
    'BABA': 'Alibaba Group Holding Limited',
    'JD': 'JD.com Inc.',
    'BAC': 'Bank of America Corporation',
    'COST': 'Costco Wholesale Corporation',
    'WFC': 'Wells Fargo & Company',
    'AMGN': 'Amgen Inc.',
    'CAT': 'Caterpillar Inc.',
}


@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/predict_stock', methods=['POST'])
def predict_stock():
    data = request.get_json()
    stock_symbol = data.get('stockSymbol')
    stock_data = yf.Ticker(stock_symbol)
    historical_data = stock_data.history(period="1y")
    closing_prices = historical_data['Close']
    train_size = int(len(closing_prices) * 0.8)
    train_data, test_data = closing_prices[:train_size], closing_prices[train_size:]

    # Explicitly set frequency when creating date index
    train_data.index = pd.date_range(start=train_data.index[0], periods=len(train_data), freq='B')
    order = (5, 1, 0)
    model = ARIMA(train_data, order=order)
    model_fit = model.fit()

    forecast_steps = len(test_data)
    forecast_index = pd.date_range(start=test_data.index[0], periods=forecast_steps, freq='B')
    forecast_series = pd.Series(model_fit.forecast(steps=forecast_steps), index=forecast_index)

    # Combine the actual data, handling NaN values
    combined_data = closing_prices.combine_first(forecast_series)

    # Handle NaN values by replacing them with None
    combined_data = combined_data.where(pd.notna(combined_data), None)

    return jsonify({
        'dates': combined_data.index.strftime('%Y-%m-%d').tolist(),
        'actual': combined_data.loc[closing_prices.index].values.tolist(),
        'fitted': model_fit.fittedvalues.tolist(),
    })


# Assuming you have a global variable for encoding mapping
encoding_mapping = {}


@app.route('/dataframe', methods=['GET', 'POST'])
def dataframe():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))

    stock_symbol = request.form.get('stockSymbol', '')
    start_date = request.form.get('startDate', '')
    end_date = request.form.get('endDate', '')

    if request.method == 'POST' and stock_symbol and start_date and end_date:
        # Fetch stock data using the fetch_stock_data function
        historical_data = fetch_stock_data(stock_symbol, start_date, end_date)

        # Data Cleaning
        historical_data = clean_data(historical_data)

        # Rescaling (Min-Max Scaling)
        historical_data = min_max_scaling(historical_data)

        # Normalization (Z-Score Standardization)
        historical_data = z_score_standardization(historical_data)

        # Encoding (Label Encoding)
        historical_data = label_encode(historical_data, 'stock_symbol')

        # Prepare DataFrame as HTML
        table_html = historical_data.to_html()

        return render_template('dataframe.html', stock_symbol=stock_symbol, start_date=start_date, end_date=end_date,
                               stock_data=historical_data, table_html=table_html)

    # Handle the GET request (render a template or provide an appropriate response)
    return render_template('dataframe.html', stock_data=None, start_date=start_date, end_date=end_date)


def fetch_stock_data(stock_symbol, start_date, end_date):
    stock_data = yf.Ticker(stock_symbol)
    stock_data = stock_data.history(start=start_date, end=end_date)
    return stock_data


def clean_data(data):
    # Implement data cleaning logic here
    # For example, drop missing values
    cleaned_data = data.dropna()
    return cleaned_data


def min_max_scaling(data):
    # Implement min-max scaling
    return (data - data.min()) / (data.max() - data.min())


def z_score_standardization(data):
    # Implement z-score standardization
    return (data - data.mean()) / data.std()


def label_encode(data, column):
    # Implement label encoding
    global encoding_mapping
    if column not in encoding_mapping:
        encoding_mapping[column] = {value: index for index, value in enumerate(data.index.unique())}

    data[column + '_encoded'] = data.index.map(encoding_mapping[column])
    return data


@app.route('/stock_list', methods=['GET'])
def stock_list():
    return render_template('stock_list.html', stock_data=stock_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            session['logged_in'] = True
            return redirect(url_for('index'))  # Redirect to the index route after successful login
        else:
            error_message = "Incorrect username or password."

    return render_template('login.html', error_message=error_message)


# Logout route
@app.route('/logout')
def logout():
    # Clear the 'logged_in' session variable
    session.pop('logged_in', None)

    # Redirect the user to the login page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
