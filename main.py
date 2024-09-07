file1 = open('information.txt', 'r')
data = file1.read()

file2 = open('information.txt', 'w')
print("File is in write mode......")
file2.write(data + " Hello I am penguin. I am cody.")

file2.close()