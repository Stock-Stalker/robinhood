FROM python:3.9-slim-buster

LABEL decription="Production image for StockStalker robinhood."

WORKDIR /usr/src/app

HEALTHCHECK --interval=1m --timeout=5s --retries=2 \
  CMD curl -f http://localhost/robinhood/AAPL || exit 1

RUN rm -r /tmp/*

RUN rm /usr/bin/expiry && rm /usr/bin/newgrp && rm /usr/bin/chsh && rm /bin/mount && \
  rm /usr/bin/chage && rm /usr/bin/chfn && rm /usr/bin/passwd && rm /usr/bin/gpasswd && \
  rm /bin/su && rm /bin/umount && rm /sbin/unix_chkpwd && rm /usr/bin/wall

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -g 999 nonroot && useradd -r -u 999 -g nonroot nonroot

USER nonroot

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
