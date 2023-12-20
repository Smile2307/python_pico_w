print("Open the file and read its contents")
fp = open("MyFile.txt", "r")
str = fp.read(80)
fp.close()
print(str)

