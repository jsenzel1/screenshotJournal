import os

number =4

with open('index.txt','r') as f:
    val = f.readline()
    intVal = int(val)
    print("current value: " + val)
	
systemString = 'screencapture -m ./caps/' + val + '.jpg'
os.system(systemString)
print(systemString)

with open('index.txt','w') as f:
        f.write(str(intVal+1))
        print("next value: "+str(intVal+1))

