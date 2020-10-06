print("--------- printing all contents of the file -----------------------")
f = open("demo-file.txt", "r")
content = f.read()
print(content)

print("--------- reading only one line -----------------------")
f1 = open("demo-file.txt", "r")
# Reading only the first line of hte file
print(f1.readline())
print("--------- reading line by line -----------------------")
f2 = open("demo-file.txt", "r")
for x in f2:
    print(x)

print("--------- closing the file -----------------------")
f3 = open("demo-file.txt", "r")
print(f3.readline())
f3.close()
print("file closed !")
