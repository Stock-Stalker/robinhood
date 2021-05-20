"""Test utils/preprocessor.py functions."""
import json
import unittest
from app import app


class TestRobinhood(unittest.TestCase):
    """Robinhood test class."""

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

    def test_get_historical(self):
        """Test get historical route."""
        symbol = "AAPL"
        span = "week"

        res = app.test_client().get(
            "/robinhood/{0}/historical/{1}".format(symbol, span)
        )
        result_json = json.loads(res.get_data().decode("utf-8"))

        self.assertIsInstance(result_json, dict)
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
