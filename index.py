import create, read, update, delete

print("\nWelcome to School Management System")

while True:
        print("\nSelect the opereations: \n1. Create \n2. Search \n3. Update \n4. Delete \n5. Exit")
        check = int(input("\nEnter your choice (1-5 only): "))
        match check:
            
            case 1:
                try:
                    print("\n1. Create a new file \n12. Create a new system ")
                    check = int(input("\nEnter your choice (1-2 only): "))
                    filename = input("Enter file name: ").lower().strip()
                    name = input("Enter system name: ").lower().strip()
                
                    match check:
                        case 1:
                            create.create_file(filename, name)
                        
                        case 2:
                            create.create_system(filename, name)
                except Exception as e:
                    print(e)
                        
            case 2:
                try:
                    print("\n1. Search file \n2. Search system \n3. Search a record by value \n4. Search all records with matching value")
                    check = int(input("\nEnter your choice (1-4 only): "))
                    filename = input("Enter file name: ").lower().strip()
                    
                    match check:
                        case 1:
                            print(read.read_file(filename))
                            
                        case 2:
                            system = input("Enter system name: ").lower().strip()
                            element, _ = read.search_system(filename, system)
                            
                        case 3:
                            system = input("Enter system name: ").lower().strip()
                            key = input("Enter the key: ").lower().strip()
                            value = input("Enter the value: ").lower().strip()
                            element, _ = read.search_by_value(filename, system, key, value)
                            print(element)
                            
                        case 4:
                            system = input("Enter system name: ").lower().strip()
                            key = input("Enter the key: ").lower().strip()
                            value = input("Enter the value: ").lower().strip()
                            element, _ = read.search_all_value(filename, system, key, value)
                            print(element)
                    
                except Exception as e:
                    print(e)
                    
            case 3:
                try:
                    print("\n1. Append record \n2. Update exisiting records ")
                    check = int(input("\nEnter your choice (1-2 only): "))
                    filename = input("Enter filename: ").lower().strip()
                    match check:
                        case 1:
                            system = input("Enter system name: ").lower().strip()
                            update.appened_file(filename, system)       
                        case 2:
                            system = input("Enter system name: ").lower().strip()
                            update.update_file(filename, system)
                            
                except Exception as e:
                    print(e)
                    
            case 4:
                try:
                    print("\n1. Delete file \n2. Delete system \n3. Delete a record by value \n4. Delete all records with matching value")
                    check = int(input("\nEnter your choice (1-4 only): "))
                    filename = input("Enter file name: ").lower().strip()
                    
                    match check:
                        case 1:
                            delete.delete_file(filename)
                            
                        case 2:
                            system = input("Enter system name: ").lower().strip()
                            delete.delete_system(filename, system)
                            
                        case 3:
                            system = input("Enter system name: ").lower().strip()
                            key = input("Enter the key: ").lower().strip()
                            value = input("Enter the value: ").lower().strip()
                            delete.delete_by_value(filename, system, key, value)
                            
                        case 4:
                            system = input("Enter system name: ").lower().strip()
                            key = input("Enter the key: ").lower().strip()
                            value = input("Enter the value: ").lower().strip()
                            delete.delete_all_value(filename, system, key, value)                            
                    
                except Exception as e:
                    print(e)
            
            case _:
                break
                