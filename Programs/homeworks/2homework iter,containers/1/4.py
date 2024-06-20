def createGenerator() :  
   a = 0
   n = 100
   mylist = range(a,n)  
   for i in mylist :
      if i % 7 == 0:
         yield i
         
mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!
for i in mygenerator:
   print(i)
