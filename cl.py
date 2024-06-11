import os
import shutil
print(dir(os))

print(os.getcwd())

#print(os.mkdir("test"))

print(os.listdir())

path = '/Users/hemanthkumar/Class102'
isExist = os.path.exists(path)

print(isExist)

path ="/Users/hemanthkumar/Class102/C102_assets-main/feather.jfif"
source ="/Users/hemanthkumar/Class102/C102_assets-main/feather.jfif"
destination = "/Users/hemanthkumar/Class102/C102_assets-main/copyfeather.jfif"
dest = shutil.copy(source,destination)
print("After copying file:")


p ="/Users/hemanthkumar/Class102/C102_assets-main/feather.jfif"
source ="/Users/hemanthkumar/Class102/C102_assets-main/feather.jfif"
destination = path ="/Users/hemanthkumar/Class102/test/feather.jfif"
destination = shutil.move(source,destination)
