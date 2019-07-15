from methods import *

def test1():
    servers = read_file("SE_test_1_servers.txt")
    print(servers)

def test2():
    serverResponse = get_server_status("https://api.github.com", "")
    print(serverResponse["user_repositories_url"])

def test2_2():
    servers = read_file("./tests/test_servers.txt")
    get_servers_status(servers,"./output/test/response.json","https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/", ".json")
    
def test3():
    servers = []
    for i in range(0,100):
        rNum = random.randint(0,40)
        servers.append("server-00" + str(rNum) + "\n")
    get_servers_status(servers,"./output/test/test_response.json","https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/", ".json")

def test4():
    write_success_rates("./output/test/test_response.json", "./output/test/test_success_rate.txt")

def test4_2():
    write_success_rates("./output/test/response.json", "./output/test/success_rate.txt")

def test5():
    group_success_rate("./output/test/test_success_rate.txt", "./output/test/test_grouped_success.json")

def test5_2():
    group_success_rate("./output/test/success_rate.txt", "./output/test/grouped_success.json")

def test6():
    compute_and_display("./output/test/test_grouped_success.json", "./output/test/test_agg.txt")

def test6_2():
    compute_and_display("./output/test/grouped_success.json", "./output/test/agg.txt")
