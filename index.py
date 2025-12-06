import create, read, appened, update, delete, search

print("Welcome to School Management System")

while True:
        check = int(input("Select the opereations: \n1. Create \n2. Read \n3.Append \n4.Update \n5.Search \n6.Delete \n7.Exit"))
        match check:
            
            case 1:
                check = int(input("1.Create a new file \n2. Create a new system"))
                filename = input("Enter file name: ").lower().strip()
                name = input("Enter system name: ").lower().strip()
                
                match check:
                    case 1:
                        create.create_file(filename, name)
                        
                    case 2:
                        create.create_system(filename, name)
                        
            case 2:
            