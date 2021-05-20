import os
import json
from datetime import datetime, date, time
import robin_stocks.robinhood as r


class Robinhood:
    isAuthentificated = False
    login_time = ""

    @classmethod
    def login(cls):
        email = os.getenv("ROBINHOOD_EMAIL")
        password = os.getenv("ROBINHOOD_PASSWORD")
        r.login(email, password)
        cls.login_time = (datetime.utcnow()).strftime("%H:%M:%S")

    @classmethod
    def check_login_time(cls):
        format = "%H:%M:%S"
        current_time = (datetime.utcnow()).strftime("%H:%M:%S")

        time_delta = abs(
            datetime.strptime(cls.login_time, format)
            - datetime.strptime(current_time, format)
        )

        # Relogin after 22 hours
        if time_delta.total_seconds() >= 79200:
            Robinhood.login()

    @classmethod
    def search_stocks(cls, query):
        Robinhood.check_login_time()

        res = r.helper.request_get(
            "https://bonfire.robinhood.com/deprecated_search/?query={}&user_origin=US".format(
                query
            ),
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
        Robinhood.check_login_time()

        current_price = r.stocks.get_latest_price(
            symbol, includeExtendedHours=False
        )

        return {"price": current_price}

    @classmethod
    def get_company_name(cls, symbol):
        Robinhood.check_login_time()

        company_name = r.stocks.get_name_by_symbol(symbol)

        return {"companyName": company_name}

    @classmethod
    def get_historical(cls, ticker, span):
        Robinhood.check_login_time()

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
            return False

        response = r.stocks.get_stock_historicals(
            ticker, interval=interval, span=span
        )

        if response[0] == None:
            return False

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
