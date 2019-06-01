FROM python:latest

COPY . /test

WORKDIR /test

CMD ["./run.py"]