from waitress import serve
from robinhood import app

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, threads=8, url_prefix='/')
