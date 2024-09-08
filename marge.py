import os
file1 = open("apple.txt" , "r")
file2 = open("banana.txt" , "r")

if os.path.exists("a2b.txt"):
    os.remove("a2b.txt")

n = open("a2b.txt" , "x")
n.write(file1.read() + "\n" + "\n" + file2.read())

n.close()
file1.close()
file2.close()
