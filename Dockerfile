FROM python:3.9-slim-buster

LABEL decription="Production image for StockStalker robinhood."

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
