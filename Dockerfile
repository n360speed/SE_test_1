FROM ubuntu:18.04

WORKDIR /SE_test_1

RUN apt-get update && apt-get install -y \
    python3.6 \
    python-pip && pip install requests

COPY . /SE_test_1