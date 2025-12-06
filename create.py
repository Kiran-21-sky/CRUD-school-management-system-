import os, json

def create_file(filename, name):
    
    if os.path.exists(filename):
        print("File already exisits")
        return
    
    data = {}    
    data.setdefault(name, [])
    
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            print(f"\nNew file created \nName of the file: {filename} \nIntialized key value: {name}")
            return
    except Exception as e:
        print(e)
        return