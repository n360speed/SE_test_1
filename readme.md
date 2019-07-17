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

Required to run:
```sh
# You should be able to use any python 3.0+ version
sudo apt install python3.6 python-pip
pip install requests
```

To run from command prompt one of the following:
```sh
python main.py
python3.6 main.py
# if you have py setup as alias you can use the following
py main.py

# You can also spin up the docker container with the following
docker build --tag se_test_1 .
docker run -it se_test_1:latest
cd /SE_test_1 # You shouldn't need to do this but states expected location
python main.py
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