#! usr/bin/env python3
dream_obj=open("Python_06.txt","r")
print(dream_obj)

for word in dream_obj:
  print(word.upper())
dream_read=open("Python_06.txt","r")
dream_write=open("Python_06_uc.txt","w")
for line in dream_read:
  line=line.rstrip()
  dream_write.write('line'+"/n")
print(dream_write)




