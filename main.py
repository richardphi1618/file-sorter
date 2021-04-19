import os
import shutil
import csv
 
csv_file = input("\nEnter your list: ") 
#csv_file = "photostofind.csv"

src_dir = input("Enter your source folder: ") 
#src_dir = "ada"

full_path = os.path.realpath(__file__)
home = os.path.dirname(full_path)
#print(home)

from_folder = home + "\\" + src_dir
to_folder = home + "\\found"
       
print("\nSearching Directory: " + from_folder)
print("Destination Directory: " + to_folder + "\n")

if not os.path.exists('found'):
    os.makedirs('found')

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    ini_list = list(reader)
    files_to_find = sum(ini_list, [])
    

for (dirpath, dirnames, filenames) in os.walk(src_dir):
    for fname in filenames:
        if fname in files_to_find:
            print (fname)
            file_in_motion = os.path.join(dirpath, fname)
            shutil.copy(file_in_motion, to_folder)