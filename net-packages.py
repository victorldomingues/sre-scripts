from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("../") if isfile(join("../", f))]

print("file")
print(onlyfiles)

print("../")
print(listdir("../"))

print("../action-net-packages")
print(listdir("../action-net-packages"))

print("../../")
print(listdir("../../"))

print("../../action-net-packages")
print(listdir("../../action-net-packages"))

print("../../../")
print(listdir("../../../"))

print("current")
print(listdir("."))

# import os
# from fnmatch import fnmatch
# import re
# import json

# root = '.'
# pattern = "*.csproj"

# def read(path, name):
#     result = []
#     file = os.path.join(path, name)
#     regex = re.compile("<PackageReference.*.Include=\"*.*\".*.Version=\".*.\".*.>")
#     with open(file) as f:
#         for line in f:
#             search = regex.search(line)
#             if search is not None :
#                 result.append(search.group()
#                                     .strip())

#     return result

# file_list = []
# for path, subdirs, files in os.walk(root):
#     print("files")
#     print(files)
#     for name in files:
#         if fnmatch(name, pattern):
#             file = {
#                 name: read(path, name)
#             }
#             file_list.append(file)
            
# print(json.dumps(file_list))


