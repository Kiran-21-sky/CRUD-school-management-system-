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
        print(f"After deletion: {element}")
        write_file(filename, content)
        return
    except Exception as e:
        print(e)
        return
    
def delete_by_codition(filename, system, condition):
    
    element, content = search_system(filename, system)
    
    target = [item for item in element if condition(item)]
    if not target:
        print(f"No matches for {condition}")
        return
    
    print(target)
    check = input("Delete all record? Y/N: ").lower().strip()
    if check == "y":
        element = [item for item in element if not condition(item)]
        print(f"After deletion: {element}")
        write_file(filename, content)
        return
    
    else:
        print("Delete a specific record? Y/N: ").lower().strip()
        if check == "y":
            while True:
                print("Enter 'stop' as key to exit")
                key = input("Enter the key value: ").strip().lower()
                if key == 'stop':
                    print(f"After deletion: {element}")
                    break
                value = input("Enter the value: ").lower().strip()
                delete_by_value(filename, system, key, value)
                
        else:
            print(f"After deletion: {element}")
            print("No record was deleted")
            return
            
def delete_all_value(filename, system, value):
    element, content = search_system(filename, system)
    
    target = [item for item in element if value in item.get(key)]
    if not target:
        print(f"No matches found for {value}")
        return
    
    print(target)
    check = input("Delete all record? Y/N: ").lower().strip()
    if check == "y":
        element = [item for item in element if value not in item.get(key) ]
        print(f"After deletion: {element}")
        write_file(filename, content)
        return
    
    else:
        print("Delete a specific record? Y/N: ").lower().strip()
        if check == "y":
            while True:
                print("Enter 'stop' as key to exit")
                key = input("Enter the key value: ").strip().lower()
                if key == 'stop':
                    print(f"After deletion: {element}")
                    break
                value = input("Enter the value: ").lower().strip()
                delete_by_value(filename, system, key, value)
                
        else:
            print(f"After deletion: {element}")
            print("No record was deleted")
            return