"""Robinhood routes."""
from . import app
from .robinhood import Robinhood
from flask_api import status

Robinhood.login()


@app.route("/robinhood/search/<query>")
def search_stocks(query):
    """Search stocks by query."""
    data = Robinhood.search_stocks(query)

    if not data:
        return "Not found", status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/price")
def get_current_price(symbol):
    """Get current price by symbol."""
    data = Robinhood.get_current_price(symbol)

    if not data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/name")
def get_company_name(symbol):
    """Take a symbol and return the company name as a string."""
    data = Robinhood.get_company_name(symbol)

    if not data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/historical/<span>")
def get_historical(symbol, span):
    """Get historial data by symbol and span."""
    historical_data = Robinhood.get_historical(symbol, span)

    if not historical_data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return historical_data
