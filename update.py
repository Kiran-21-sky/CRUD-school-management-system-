import read
from write import write_file

def update_file(filename, system):

    ele_key = input("Enter the key: ").strip().lower()
    ele_value = input("Enter the value: ").lower().strip()
    
    edit, data = read.search_by_value(filename, system, ele_key, ele_value)
    if not edit:
        print("Key or Value does not exists \nUpdation failed")
        return 
    
    print(f"Before updation: {edit}")
    
    while True:        
        ele_key = input("Enter the key: ").strip().lower()
        ele_value = input("Enter the new value:").lower().strip()
        edit[ele_key] = ele_value
        print(f"After updation: {edit}")
        check = input("Do want to update other values? Y/N : ").lower().strip()
        if check == "n":
            break
    
    check = input("Do you want to save changes? Y/N : ").lower().strip()
    if check == "y":
        write_file(filename, data)
        print("Updation successful")
        return
    
def appened_file(filename, system):
    
    content = read.read_file(filename)
    element = content.get(system)
    if not isinstance(element, list):
        element = []
        content[system] = element
        print("New system created")
    element.append({})
    new_entry = element[-1]
    
    try:
        while True:
            print("Enter key and values. Enter 'stop' to finish.")
            key = input("Enter key: ").lower().strip()
            if key == 'stop':
                break
            value = input("Enter value: ").strip()
            new_entry[key] = value
            print(f"Added --> {key}: {value}")
    except Exception as e:
        print(e)
        return