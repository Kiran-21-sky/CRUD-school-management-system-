import os, read, write, json

def create_file(filename, name):
    
    if os.path.exists(filename):
        print("File already exisits")
        return
    
    data = {}    
    data.setdefault(name, [])

    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nNew file created \nFile name: {filename} \nSystem name: {name}")
        return
    except Exception as e:
        print(e)
        return

    
    
def create_system(filename, system_name):
    
    if not os.path.exists(filename):
        print("\nFile does not exist")
        return
    
    content = read.read_file(filename)
    if not isinstance(system_name, list):
        element = []
        content[system_name] = element
        print(f"New system created: \n{content}")
        write.write_file(filename, content)
    else:
        print(f"{system_name} already exist")
        return