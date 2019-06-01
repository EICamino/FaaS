FROM python:latest

COPY . /test

WORKDIR /test

CMD ["./fib.py", "10"]