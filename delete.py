from search import *
from write import write_file

def delete_system(filename, system):
    
    element, content = search_system(filename, system)
    
    try:
        content.remove(element) 
    except Exception as e:
        print(e)
        return
    
    write_file(filename, content)
    print("Deletion Successful")
    return

def delete_by_value(filename, system, key, value):
    
    element, content = search_by_value(filename, system, key, value)
    
    if not element:
        return
    
    try:
        content.remove(element)
        write_file(filename, content)
        return
    except Exception as e:
        print(e)
        return
    
def delete_by_codition(filename, system, condition):
    
    element, content = search_by_condition(filename, system, condition)
    
    if not element:
        return
    
    print(element)
    check = input("Delete all elements? Y/N: ").lower().strip()
    if check == "y":
        element = [item for item in content if item.get("id") not in element.get("id")]
        content[system] = element
        write_file(filename, content)
        