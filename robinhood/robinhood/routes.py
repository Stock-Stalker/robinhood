from . import app
from .robinhood import Robinhood
from flask_api import status

Robinhood.login()


@app.route("/robinhood/search/<query>")
def search_stocks(query):
    data = Robinhood.search_stocks(query)

    if not data:
        return "Not found", status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/price")
def get_current_price(symbol):
    """Takes any number of symbols separated by a , and returns the latest price of each one as a string."""
    data = Robinhood.get_current_price(symbol)

    if not data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/name")
def get_company_name(symbol):
    """Takes a symbol and return the company name as a string."""
    data = Robinhood.get_company_name(symbol)

    if not data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>")
def get_stock(symbol):
    data = Robinhood.get_stock(symbol)

    if not data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return data


@app.route("/robinhood/<symbol>/historical/<span>")
def get_historical(symbol, span):
    historical_data = Robinhood.get_historical(symbol, span)

    if not historical_data:
        return "{} not found".format(symbol), status.HTTP_400_BAD_REQUEST

    return historical_data
