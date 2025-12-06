import read

def search_system(filename, system):
    content = read.read_file(filename)
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