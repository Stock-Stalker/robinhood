FROM python:3.9

LABEL decription="Production image for StockStalker robinhood."

WORKDIR /usr/src/app

COPY predictor/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY predictor .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
