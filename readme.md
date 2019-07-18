<h3>
I wanted to say that I never used python before, but thought it would be a great way to showcase
my skills in using unfamiliar languages to accomplish the task
</h3>

Clone repo to local work area:
```sh
git clone https://github.com/n360speed/SE_test_1.git
cd SE_test_1
```

Assumptions:
  * You have extracted the contents of this project
  * You have cd to the extracted directory
  * If you run outside of contianer, you have ran the
  following, to fix \r
    ```sh
    cat process.sh | tr -d '\r' >> process2.sh && mv -f process2.sh process.sh && chmod u+x process.sh
    
    cat SE_test_1_servers.txt | tr -d '\r' >> SE_test_1_servers.txt2 && mv -f SE_test_1_servers.txt2 SE_test_1_servers.txt
    
    cat ./tests/test_servers.txt | tr -d '\r' >> ./tests/test_servers.txt2 && mv -f ./tests/test_servers.txt2 ./tests/test_servers.txt
    
    cat main.py | tr -d '\r' >> main.py2 && mv -f main.py2 main.py
    ```


Required to run:
```sh
sudo apt install python3.6 python-pip python3-pip
pip install requests && pip3 install requests
# If you run batch script these will need to be installed
sudo apt install curl bc
```

To run from command prompt one of the following:
```sh
python main.py
python3.6 main.py
# if you have py setup as alias you can use the following
py main.py
./main.py

# You can also spin up the docker container with the following
docker build --tag se_test_1 .
docker run -it se_test_1:latest
cd /SE_test_1 # You shouldn't need to do this but states expected location
python main.py
./main.py

# You can also use the batch script, which has about the same logic
./process.sh SE_test_1_servers.txt
```

To run tests, not pass fail, but way to test my logic:
```sh
python main.py test
cat ./output/test/test_agg.txt | awk '{print $1 "    " $2 "    " $3}'
cat ./output/test/agg.txt | awk '{print $1 "    " $2 "    " $3}'
```

You might want to take a look at the different tags, to see
some progression
```sh
git tag -l
git checkout <tagName>
```

To test Bash script
```sh
./process.sh tests/test_servers.txt "https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/" ".json"
cat ./output/bash/agg.txt | awk '{print $1 "    " $2 "    " $3}'
```
