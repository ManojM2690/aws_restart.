# with open ("preproinsulin-seq.txt") as newfile:
#   xyz = newfile.read()
#   print(xyz)

# abc =open("preproinsulin-seq.txt")
# print(abc.read())
# abc.close()

print("Hello is my diary: \n ")
f1=open("files/diary.txt","r")
print(f1.read())
f1.close()

print("\nNow let's create another diary: \n ")
f2=open("files/diary2.txt","w")
f2.write("writing in my diary file!")
f2.close()