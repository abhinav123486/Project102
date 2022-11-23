import shutil
import os
from_dir, to_dir = "C:/Users/abhinav/Downloads", "C:/Users/abhinav/OneDrive/Desktop"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    name, extension = os.path.splitext(file)
    if extension == '':
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + file
        if os.path.exists(path2):
            print("Moving " + file + ".....")

            # Move from path1 ---> path3
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file + ".....")
            shutil.move(path1, path3)