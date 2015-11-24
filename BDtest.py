from bsddb3 import db 
database = db.DB() 
database.open("sc.idx")

cur = database.cursor() 
iter = cur.set(b'4.0')
while iter:
 print(iter)
 iter = cur.next_dup() 
cur.close()

#cur = database.cursor() 
#iter = cur.first()
#while iter:
 #print(iter)
 #iter = cur.next() 
#cur.close()

database.close()