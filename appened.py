import read, write

def appened_file(filename, system):
    
    content = read.read_file(filename)
    element = content.get(system)
    if not isinstance(element, list):
        element = []
        content[system] = element
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
    
    if not new_entry:
        element.pop()
        print("No element added")
        return
    
    print(content)
    write.write_file(filename, content)
    print("New data added successfully.")
    return