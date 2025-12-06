import json, os
    
def write_file(filename, data):
    
    if not os.path.exists(filename):
        print("File does not exists")
        return
    
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return
    except Exception as e:
        print(e)