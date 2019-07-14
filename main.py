#!/usr/bin/python3

import requests, sys, json, random

def read_file(filename):
    lines = ""
    with open(filename,"r") as f:
        lines = f.readlines()
    return lines

def read_file_for_json(filename):
    lines = ""
    with open(filename,"r") as f:
        lines = f.read()
    return lines

def get_server_status(server, api_endpoint = "/status"):
    url = server + api_endpoint
    data = requests.get(url).json()
    return data

def purge_file(filename = "response.txt"):
    with open(filename, "w") as f:
        f.write("")

def write_to_file(content, filename = "response.txt"):
    with open(filename, "a") as f:
        f.write(content)

def get_servers_status(servers):
    purge_file("response.json") 
    jToFile = json.loads("[]")
    
    for server in servers:
        try:
            f = get_server_status("http://" + server)
            jToFile.append(f.replace("[","").replace("]",""))
        except:
            print("No response from " + server)

    purge_file("response.json")
    write_to_file(str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n",""), "response.json")

def write_success_rates(readfile="response.json", writefile="success_rate.txt"):
    responses = read_file_for_json(readfile)
    jsonRes = json.loads(responses)
    purge_file(writefile)
    for j in jsonRes:
        app = j["Application"]
        ver = j["Version"]
        req = float(j["Request_Count"])
        sec = float(j["Success_Count"])
        result = app + " \t" + ver + " \t"  + str(req) + " \t" \
            + str(sec) + "\n"
        write_to_file(result,writefile)

def group_success_rate(readfile="success_rate.txt", writefile="grouped_success.json"):
    successRates = read_file(readfile)
    groups = []
    for successRate in successRates:
        items = successRate.replace("\n","").split(" \t")
        key = items[0] + "_" + items[1]

        i = 0
        found = False
        for group in groups:
            if groups[i].get(key):
                found = True

                rc = float(groups[i].get(key)['Request_Count']) + float(items[2])
                sc = float(groups[i].get(key)["Success_Count"]) + float(items[3])

                groups[i].get(key).update({"Request_Count": rc })
                groups[i].get(key).update({"Success_Count":  sc })
                break
            i = i + 1
        
        if not found:
            groups.append({ key : {"Request_Count": items[2], \
                "Success_Count": items[3]}})
                    
    purge_file(writefile)
    write_to_file(json.dumps(groups),writefile)

def compute_and_display(readfile="grouped_success.json", writefile="agg.txt"):
    testGrouped = read_file_for_json(readfile)
    
    purge_file(writefile)
    for output in json.loads(testGrouped):
        sp = json.dumps(output.keys()).replace("\"","").replace("[","").replace("]","").split("_")
        na = sp[0]
        vr = sp[1]
        result = json.loads(json.dumps(output.values()))
        rc = result[0].get("Request_Count")
        sc = result[0].get("Success_Count")
        
        print(na + " \t" + vr)
        actualSr = float(sc) / float(rc)
        print("   success rate: " + str(actualSr) )
        write_to_file(na + " \t" + vr + " \t" + str(actualSr) + "\n", writefile)
    
def test1():
    servers = read_file("SE_test_1_servers.txt")
    print(servers)

def test2():
    serverResponse = get_server_status("https://api.github.com", "")
    print(serverResponse["user_repositories_url"])

def test3():
    jToFile = json.loads("[]")
    f = read_file("SE_test_1_responses.txt")
    for i in range(0,500):
        rNum = random.randint(0,999)
        jToFile.append(f[rNum].replace("[","").replace("]",""))
    purge_file("test_response.json")
    write_to_file(str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n",""), "test_response.json")

def test4():
    write_success_rates("test_response.json", "test_success_rate.txt")

def test5():
    group_success_rate("test_success_rate.txt", "test_grouped_success.json")

def test6():
    compute_and_display("test_grouped_success.json", "test_agg.txt")

if sys.argv.__contains__("test"):
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
else:
    # Read server file
    servers = read_file("SE_test_1_servers.txt")
    
    # Get API request for servers
    get_servers_status(servers)
    
    # Write Success Rate Not Grouped
    write_success_rates()

    # Group by Application and Version
    group_success_rate()

    # Compute and Display the results
    compute_and_display()