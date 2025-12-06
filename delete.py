from read import *
from write import write_file
import os

def delete_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"File {filename} deleted successfully")
            return
        except Exception as e:
            print(e)
    else:
        print(f"File {filename} does not exists")
        return
    
def delete_system(filename):
    content = read_file(filename)
    if not content:
        print("\nFile is empty")
        return 
    system = input("\nEnter system name: ").lower().strip()
    
    try:
        del content[system] 
    except Exception as e:
        print(e)
        return
    
    write_file(filename, content)
    print("Deletion Successful")
    return

def delete_by_value(filename):
    element, content = search_system(filename)
    if not element:
        return
    key = input("Enter key: ").lower().strip()
    value = input("Enter value: ").lower().strip()
    target = next((item for item in element if value in item.get(key)), None)
    if not target:
        print("Value not found")
        return 
    try:
        element.remove(target)
        print(f"After deletion: {element}")
        write_file(filename, content)
        return
    except Exception as e:
        print(e)
        return
    
def delete_all_value(filename):
    content = read_file(filename)
    if not content:
        print("\nFile is empty")
        return 
    system = input("\nEnter system name: ").lower().strip()
    element = content.get(system, [])
    if not element:
        print("\nSystem not found")
        return
    
    key = input("Enter key: ").lower().strip()
    value = input("Enter value: ").lower().strip()
    target = [item for item in element if value in item.get(key)]
    if not target:
        print(f"No matches found for {value}")
        return
    
    print(target)
    check = input("Delete all record? Y/N: ").lower().strip()
    if check == "y":
        element = [item for item in element if value not in item.get(key)]
        print(f"After deletion: {element}")
        content[system] = element
        write_file(filename, content)
        return
    
    else:
        check = input("Delete a specific record? Y/N: ").lower().strip()
        if check == "y":
            while True:
                print("Enter 'stop' as key to exit")
                key = input("Enter the key value: ").strip().lower()
                if key == 'stop':
                    print(f"After deletion: {element}")
                    return
                value = input("Enter the value: ").lower().strip()
                delete_by_value(filename)
                
        else:
            print(f"After deletion: {element}")
            print("No record was deleted")
            return