import os
import json

def read_file(filename):
    
    if not os.path.exists(filename):
        print("File does not exisits")
        return {}
    
    with open(filename, "r") as f:
        data = f.read().strip()
        if not data:
            return {}
        
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print("File Error")
        return {}
        