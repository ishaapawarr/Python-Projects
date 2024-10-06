s = "Isha is a good girl"
#Writing to a file
#with open("text.txt", "w") as f:
#  f.write(s)
#fp = open("test.txt", "w")
#fp.write(s)
#fp.close()

#Reading to a file
# with open("isha.txt", "r") as f:
#  s = f.read()
#  print(s)

# f = open("isha.txt", "r")
# s = f.read()
# print(s)
# f.close()

#Appending to a file
with open("isha.txt", "a") as f:
  f.write("I am writing this")

#fp = open("test.txt", "w")
#fp.write(s)
#fp.close()