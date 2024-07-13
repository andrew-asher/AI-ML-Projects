# Intelligent Stock Trader (IST) Platform

## Overview

The Intelligent Stock Trader (IST) Platform is a Flask-based application designed to forecast stock prices using historical data fetched from `yfinance` and processed with ARIMA (AutoRegressive Integrated Moving Average) models.

## Features

- **Dynamic Stock Price Forecasting**: Utilizes historical stock data to predict future closing prices.
- **ARIMA Model**: Fits an ARIMA model to historical data for time-series forecasting.
- **REST API**: Provides a RESTful API endpoint (`/predict_stock`) to receive POST requests with stock symbols and return forecasted stock prices.

## Setup Instructions

To run the application locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Intelligent-Stock-Trader.git
   cd Intelligent-Stock-Trader
pip install -r requirements.txt
python app.py

## Dependencies

Flask: Web framework for Python
yfinance: Fetches stock market data
pandas: Data manipulation library
numpy: Scientific computing library
statsmodels: Statistical models and tests

## Example Usage

Assuming the application is running locally:

1. Send a POST request to http://localhost:5000/predict_stock with a JSON payload containing a valid stock symbol.
2. Receive a JSON response containing actual and forecasted closing prices.
