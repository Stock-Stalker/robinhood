"""Robinhood routes."""
from flask_api import status
from . import app
from .robinhood import Robinhood
from .utils import alpha_string, alphanumeric_string


@app.route("/robinhood/search/<query>")
def search_stocks(query):
    """Search stocks by query."""
    sanitized_query = alpha_string(query)
    data = Robinhood.search_stocks(sanitized_query)
    return data


@app.route("/robinhood/<symbol>/price")
def get_current_price(symbol):
    """Get current price by symbol."""
    if len(symbol) > 5:
        return "symbol exceeded length", status.HTTP_400_BAD_REQUEST
    sanitized_symbol = alpha_string(symbol)
    data = Robinhood.get_current_price(sanitized_symbol)
    return data


@app.route("/robinhood/<symbol>/name")
def get_company_name(symbol):
    """Take a symbol and return the company name as a string."""
    if len(symbol) > 5:
        return "symbol exceeded length", status.HTTP_400_BAD_REQUEST
    sanitized_symbol = alpha_string(symbol)
    data = Robinhood.get_company_name(sanitized_symbol)
    return data


@app.route("/robinhood/<symbol>/historical/<span>")
def get_historical(symbol, span):
    """Get historial data by symbol and span."""
    if len(symbol) > 5:
        return "symbol exceeded length", status.HTTP_400_BAD_REQUEST
    if len(span) > 6 or len(span) < 3:
        return "span wrong length", status.HTTP_400_BAD_REQUEST
    sanitized_symbol = alpha_string(symbol)
    sanitized_span = alphanumeric_string(span)
    historical_data = Robinhood.get_historical(
        sanitized_symbol, sanitized_span
    )
    return historical_data
