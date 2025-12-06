import os
import json

def read_file(filename):
    
    if not os.path.exists(filename):
        print("File does not exisits")
        return {}
    
    with open(filename, "r") as f:
        data = f.read().strip()
        if not data:
            return {}
        
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print("File Error")
        return {}
        
def search_system(filename):
    content = read_file(filename)
    if not content:
        print("\nFile is empty")
        return {}
    system = input("\nEnter system name: ").lower().strip()
    element = content.get(system, [])
    if not element:
        print("System not found")
        return []

    return element, content

def search_by_value(filename):
    element, _ = search_system(filename)
    if not element:
        return []
    key = input("Enter key: ").lower().strip()
    value = input("Enter value: ").lower().strip()
    target = next((item for item in element if value in item.get(key)), None)
    if not target:
        print("Value not found")
        return []
    return target

def search_all_value(filename):
    element, _ = search_system(filename)
    if not element:
        return []
    key = input("Enter key: ").lower().strip()
    value = input("Enter value").lower().strip()   
    target = [item for item in element if value in item.get(key)]
    if not target:
        print("Value not found")
        return
    return target