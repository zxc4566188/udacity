import os
def rename_files():
    file_list=os.listdir(r"C:\Users\USER1\Desktop\my python\prank\prank")
    print(file_list)
    os.chdir(r"C:\Users\USER1\Desktop\my python\prank\prank")
    for file_name in file_list:
        print(file_name)
        os.rename(file_name, file_name.strip("0123456789"))
rename_files()
    
        
