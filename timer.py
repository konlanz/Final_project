from datetime import datetime
start=datetime.now()

#Statements

count = 0
while count <= 7:
    count += 1
    
stop = datetime.now()
print (stop-start)