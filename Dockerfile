FROM python:3.6.4

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /app

COPY . /app/

WORKDIR /app
RUN pip install -r requirements.txt

RUN chmod +x *.sh
ENTRYPOINT ["./entrypoint.sh"]


