import os
def rename_files():
    file_list = os.listdir('C:\Users\Owner\Documents\prank')
    print(file_list)
    os.chdir('C:\Users\Owner\Documents\prank')

    #rename old file names with the code below

    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files() 
