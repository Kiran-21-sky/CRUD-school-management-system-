import os, read, write, json

def create_file(filename):
    
    if os.path.exists(filename):
        print("File already exisits")
        return
    
    data = {}    

    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nNew file created \nFile name: {filename} ")
        return
    except Exception as e:
        print(e)
        return
    
def create_system(filename):
    
    if not os.path.exists(filename):
        print("\nFile does not exist")
        return
    
    content = read.read_file(filename)
    system_name = input("\nEnter system name: ").lower().strip()
    if not isinstance(system_name, list):
        element = []
        content[system_name] = element
        print(f"New system created: \n{content}")
        write.write_file(filename, content)
    else:
        print(f"{system_name} already exist")
        return