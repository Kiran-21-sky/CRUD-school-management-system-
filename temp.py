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
        
def search_system(filename, system):
    content = read_file(filename)
    if not content:
        print("File is empty")
        return {}
    
    element = content.get(system, [])
    if not element:
        print("System not found")
        return []

    return element, content

def search_by_value(filename, system, key, value):
    element, content = search_system(filename, system)
    target = next((item for item in element if item.get(key) in value), None)
    if not target:
        print("Value not found")
        return []
    return target, content

def search_by_condition(filename, system, condition):
    element, content = search_system(filename, system)
    target = [item for item in element if condition(item)]
    if not target:
        print("No item matches the given condition")
        return
    return target, content

def search_all_value(filename, system, key, value):
    element, content = search_system(filename, system)
    target = [item for item in element if value in item.get(key)]
    if not target:
        print("Value not found")
        return
    return target, content