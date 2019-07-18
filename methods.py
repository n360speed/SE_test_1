import requests, sys, json, random, os
from itertools import groupby

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
    print(url)
    data = requests.get(url).json()
    return data

def purge_file(filename = "./output/response.txt"):
    with open(filename, "w") as f:
        f.write("")

def create_dir(dir="./output/test"):
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_to_file(content, filename = "./output/response.txt"):
    with open(filename, "a") as f:
        f.write(content)

def get_servers_status(servers, filename="./output/response.json", url_prefix="http://", api="/status"):
    jToFile = json.loads("[]")
    
    for server in servers:
        try:
            f = get_server_status(url_prefix + server.strip(), api)
            j = json.dumps(f)
            jToFile.append(j)
        except:
            print("No response from " + server)

    purge_file(filename)
    value = str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n","")
    write_to_file(value, filename)

def write_success_rates(readfile="./output/response.json", writefile="./output/success_rate.txt"):
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

def group_success_rate(readfile="./output/success_rate.txt", writefile="./output/grouped_success.json"):
    successRates = read_file(readfile)
    result = []
    
    groups = groupby(successRates, lambda successRate: (successRate.split(" \t")[0] + "_"  + successRate.split(" \t")[1]))
    print(groups)
    for key, group in groups:
        print('key', key)
        rc = 0
        sc = 0
        for content in group:
            print('\t', content)
            sp = content.split(" \t")
            rc += float(sp[2])
            sc += float(sp[3])
        result.append({ key : {"Request_Count": rc, \
            "Success_Count": sc}})

    purge_file(writefile)
    write_to_file(json.dumps(result),writefile)

def compute_and_display(readfile="./output/grouped_success.json", writefile="./output/agg.txt"):
    testGrouped = read_file_for_json(readfile)
    
    purge_file(writefile)
    for output in json.loads(testGrouped):
        sp = json.dumps(output.keys()).replace("[\"","").replace("\"]","").split("_")
        na = sp[0]
        vr = sp[1]
        result = json.loads(json.dumps(output.values()))
        rc = result[0].get("Request_Count")
        sc = result[0].get("Success_Count")
        
        print(na + " \t" + vr)
        actualSr = float(sc) / float(rc)
        print("   success rate: " + str(actualSr) )
        write_to_file(na + " \t" + vr + " \t" + str(actualSr) + "\n", writefile)
