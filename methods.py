import requests, sys, json, random, os

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

def get_servers_status(servers):
    purge_file("./output/response.json") 
    jToFile = json.loads("[]")
    
    for server in servers:
        try:
            f = get_server_status("http://" + server.strip())
            jToFile.append(f)
        except:
            print("No response from " + server)

    purge_file("./output/response.json")
    write_to_file(str(jToFile).replace(r"'","").replace("\\n,","\n").replace(",\\n",""), "./output/response.json")

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

def compute_and_display(readfile="./output/grouped_success.json", writefile="./output/agg.txt"):
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
