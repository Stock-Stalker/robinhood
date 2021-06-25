FROM python:3.9-slim-buster AS build

LABEL decription="Production image for StockStalker robinhood."

WORKDIR /usr/src/app

RUN apt-get -qq update && \
  apt-get -qqy --no-install-recommends install binutils=2.31.1-16

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==21.1.2 && \
  pip install --no-cache-dir -r requirements.txt &&  \
  pip install --no-cache-dir pyinstaller==4.3

COPY . .

RUN pyinstaller wsgi.spec

FROM gcr.io/distroless/python3:nonroot

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/dist ./dist

HEALTHCHECK --interval=1m --timeout=5s --retries=2 \
  CMD curl -f http://localhost/robinhood/AAPL/name || exit 1

ENTRYPOINT [ "dist/wsgi/wsgi" ]
