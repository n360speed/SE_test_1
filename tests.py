from methods import *

def test_get_servers_status(servers):
    purge_file("./output/test/response.json") 
    jToFile = json.loads("[]")
    
    for server in servers:
        try:
            # print("https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/" + server + ".json")
            f = get_server_status("https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/" + server.strip() + ".json", "")
            #"https://raw.githubusercontent.com/n360speed/SE_test_1/master/tests/server-0001json"
            jToFile.append(f)
        except:
            print("No response from " + server)

    purge_file("./output/test/response.json")
    write_to_file(str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n",""), "./output/test/response.json")

def test1():
    servers = read_file("SE_test_1_servers.txt")
    print(servers)

def test2():
    serverResponse = get_server_status("https://api.github.com", "")
    print(serverResponse["user_repositories_url"])

def test2_2():
    servers = read_file("./tests/test_servers.txt")
    test_get_servers_status(servers)
    
def test3():
    jToFile = json.loads("[]")
    f = read_file("SE_test_1_responses.txt")
    for i in range(0,500):
        rNum = random.randint(0,999)
        jToFile.append(f[rNum].replace("[","").replace("]",""))
    purge_file("./output/test/test_response.json")
    write_to_file(str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n",""), "./output/test/test_response.json")

def test4():
    write_success_rates("./output/test/test_response.json", "./output/test/test_success_rate.txt")

def test5():
    group_success_rate("./output/test/test_success_rate.txt", "./output/test/test_grouped_success.json")

def test6():
    compute_and_display("./output/test/test_grouped_success.json", "./output/test/test_agg.txt")
