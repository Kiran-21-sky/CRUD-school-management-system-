import read
from write import write_file

def update_file(filename):

    element, data = read.search_system(filename)    
    if not element:
        return 
    key = input("Enter key: ").lower().strip()
    value = input("Enter value: ").lower().strip()
    target = next((item for item in element if value in item.get(key)), None)
    if not target:
        print("Value not found")
        return 
    
    print(f"Before updation: {target}")
    
    while True:        
        ele_key = input("Enter the key: ").strip().lower()
        ele_value = input("Enter the new value: ").lower().strip()
        target[ele_key] = ele_value
        print(f"After updation: {target}")
        check = input("Do want to update other values? Y/N : ").lower().strip()
        if check == "n":
            break
    
    check = input("Do you want to save changes? Y/N : ").lower().strip()
    if check == "y":
        write_file(filename, data)
        print("Updation successful")
        return
    
def appened_file(filename):
    
    content = read.read_file(filename)
    if not content:
        return
    system = input("Enter system: ").lower().strip()
    element = content.get(system)
    if not isinstance(element, list):
        element = []
        content[system] = element
        print("New system created")
    while True:
        element.append({})
        new_entry = element[-1]
    
        try:
            while True:
                print("\nEnter key and values. Enter 'stop' to exit.")
                key = input("Enter key: ").lower().strip()
                if key == 'stop':
                    if new_entry:
                        write_file(filename, content)
                        check = input("Do you want to add a new record? Y/N: ").lower().strip()
                        if check == "y":
                            break
                        else:
                            return
                    else:
                        element.pop()
                        return
                value = input("Enter value: ").strip()
                new_entry[key] = value
                print(f"Added --> {key}: {value}")
        except Exception as e:
            print(e)
            return