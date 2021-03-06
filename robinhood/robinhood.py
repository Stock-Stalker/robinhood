"""Robinhood util functions."""
import os
from datetime import datetime
from flask_api import status
import robin_stocks.robinhood as r


class Robinhood:
    """Robinhood class."""

    isAuthentificated = False
    login_time = ""

    @classmethod
    def login(cls):
        """Login to Robinhood."""
        email = os.getenv("ROBINHOOD_EMAIL")
        password = os.getenv("ROBINHOOD_PASSWORD")
        r.login(email, password)
        cls.login_time = (datetime.utcnow()).strftime("%H:%M:%S")

    @classmethod
    def search_stocks(cls, query):
        """
        Search stocks by query.

        :param query: the search query
        :returns: an object that contains result
        """
        Robinhood.login()
        search_url = "https://bonfire.robinhood.com/deprecated_search/"

        res = r.helper.request_get(
            "{}?query={}&user_origin=US".format(search_url, query),
            "regular",
        )

        stocks = []
        for stock in res["instruments"]:
            stocks.append(
                {
                    "symbol": stock["symbol"],
                    "companyName": stock["simple_name"],
                }
            )

        return {"results": stocks}

    @classmethod
    def get_current_price(cls, symbol):
        """
        Get current price by symbol.

        :param symbol: stock symbol to get current price
        :returns: an object that contains price
        """
        Robinhood.login()

        current_price = r.stocks.get_latest_price(
            symbol, includeExtendedHours=False
        )

        return {"price": current_price}

    @classmethod
    def get_company_name(cls, symbol):
        """
        Get company name by symbol.

        :param symbol: stock symbol to get company name
        :returns: an object that contains companyName
        """
        Robinhood.login()

        company_name = r.stocks.get_name_by_symbol(symbol)

        return {"companyName": company_name}

    @classmethod
    def get_historical(cls, ticker, span):
        """
        Get historical data by ticker and span.

        :param ticker: stock ticker to get historical data
        :param span: span of time for historical data
        :returns: an object that contains historical
        """
        Robinhood.login()

        interval = ""

        if span == "day":
            interval = "5minute"
        elif span == "week":
            interval = "hour"
        elif span == "3month":
            interval = "day"
        elif span == "year":
            interval = "day"
        elif span == "5year":
            interval = "week"
        else:
            return "{} not valid".format(span), status.HTTP_400_BAD_REQUEST

        response = r.stocks.get_stock_historicals(
            ticker, interval=interval, span=span
        )

        historical = []
        for day in response:
            historical.append(
                {
                    "date": day["begins_at"],
                    "open": day["open_price"],
                    "close": day["close_price"],
                }
            )

        return {"historical": historical}
