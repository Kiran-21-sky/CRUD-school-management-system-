from search import search_by_value
from write import write_file

def update_file(filename, system):

    ele_key = input("Enter the key: ").strip().lower()
    ele_value = input("Enter the value: ").lower().strip()
    
    edit, data = search_by_value(filename, system, ele_key, ele_value)
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