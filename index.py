import create, read, appened, write, update, delete

# create.create_file("user.json", "user_list")
print(read.read_file("user.json"))
#appened.appened_file("user.json", "admin_list")
#update.update_file("user.json", "admin_list")
delete.delete_system("user.json", "admin_list")
print(read.read_file("user.json"))
