"""Test robinhood/routes.py functions."""
import json
import unittest
from app import app


class TestRoutes(unittest.TestCase):
    """Routes test class."""

    def test_search_stocks(self):
        """Test search stocks route."""
        query = "AAPL"

        res = app.test_client().get("/robinhood/search/{0}".format(query))
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_current_price(self):
        """Test get current price route."""
        symbol = "AAPL"

        res = app.test_client().get("/robinhood/{0}/price".format(symbol))
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_company_name(self):
        """Test get company name route."""
        symbol = "AAPL"
        expected_company_name = "Apple"

        res = app.test_client().get("/robinhood/{0}/name".format(symbol))
        expected_json = {"companyName": expected_company_name}
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertEqual(expected_json, result_json)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_day(self):
        """Test get historical route for day."""
        symbol = "AAPL"
        span = "day"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_week(self):
        """Test get historical route for week."""
        symbol = "AAPL"
        span = "week"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_3month(self):
        """Test get historical route for 3month."""
        symbol = "AAPL"
        span = "3month"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_year(self):
        """Test get historical route for year."""
        symbol = "AAPL"
        span = "year"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_5year(self):
        """Test get historical route for 5year."""
        symbol = "AAPL"
        span = "5year"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)

    def test_get_historical_error(self):
        """Test get historical route for bad span."""
        symbol = "AAPL"
        span = "decade"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )

        self.assertEqual(res.status_code, 400)
