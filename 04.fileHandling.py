#FILE HANDLING 
#BASIC OPEN AND CLOSE 
"""
file = open("example.txt","w")
file.write("Hello,World")
file.close()


with open("example.txt", "r") as file:
  print(file.read())

with open("example.txt","a")as file:
  file.write("\n new line")


"""

with open("example.txt", "r") as file:
  print("FULL content:")
  for line in file:
    print(line)