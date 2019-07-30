FROM ubuntu:18.04

WORKDIR /SE_test_1

RUN apt-get update && apt-get install -y \
    python3.6 \
    python-pip \
    curl \
    python3-pip \
    bc && \
    pip install requests && \
    pip3 install requests && \
    pip install futures

COPY . /SE_test_1

RUN cat process.sh | tr -d '\r' >> process2.sh && mv -f process2.sh process.sh && chmod u+x process.sh

RUN cat SE_test_1_servers.txt | tr -d '\r' >> SE_test_1_servers.txt2 && mv -f SE_test_1_servers.txt2 SE_test_1_servers.txt

RUN cat ./tests/test_servers.txt | tr -d '\r' >> ./tests/test_servers.txt2 && mv -f ./tests/test_servers.txt2 ./tests/test_servers.txt

RUN cat main.py | tr -d '\r' >> main.py2 && mv -f main.py2 main.py && chmod u+x main.py
