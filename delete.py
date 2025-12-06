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