import os

number =4

val='0'
intVal=0

with open('int.txt','r') as f:
    val = f.readline()
    intVal = int(val)
    print("current value: " + val)
	
systemString = 'screencapture -m ./caps/' + val + '.jpg'
os.system(systemString)
print(systemString)



appString ='date >> ./dates.txt'
os.system(appString)


with open('int.txt','w') as f:
        f.write(str(intVal+1))
        print("next value: "+str(intVal+1))

