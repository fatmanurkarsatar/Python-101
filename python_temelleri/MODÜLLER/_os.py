import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir("C:\\")
# os.chdir("../..")

# klasör oluşturma
# result = os.mkdir("newdirectory")
# os.makedirs("C:\\newdirectory/yeniklasör")

# etkin dizin öğrenme
# result = os.getcwd()

# # listeleme
# result = os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

# result = os.stat("datetime.py")
# # result = result.st_size/1024
result = datetime.datetime.fromtimestamp(result.st_ctime)   #oluşturulma tarihi
result = datetime.datetime.fromtimestamp(result.st_atime)   #son erişilme tarihi
result = datetime.datetime.fromtimestamp(result.st_mtime)   #değiştirilme tarihi


print(result)