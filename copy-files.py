import os

import shutil

path = "C:\\files\\PyMediaSort\\original Folder"


#list files and folders in PATH

print ("Before copying file: ")
print(os.listdir(path))

#source path
source = "C:\\files\\PyMediaSort\\original Folder/IMG-20250426-WA0120.jpg"

#print the metadata of source file

metadata = os.stat(source)
print ("Metadata:", metadata, "\n")

#destination
destination = "C:\\files\\PyMediaSort\destinationLoc"

#copy from source to dest

dest = shutil.copy2(source, destination)