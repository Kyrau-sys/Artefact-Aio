import json




def writter_key(license_key):
    key = "static\\infos\\key\\key.json"


    with open(key, "w+") as file:
        writer = { "key" : f"{license_key}"}
        json.dump(writer, file)

    with open(key, "r+") as file:
        data = json.load(file)
    
    print(data)

