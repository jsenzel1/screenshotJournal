import os

number =4

val='0'
intVal=0

with open('/Users/Jonah/githubProjects/screenshotJournal/int.txt','r') as f:
    val = f.readline()
    intVal = int(val)
    print("current value: " + val)
	
systemString = 'screencapture -m /Users/Jonah/githubProjects/screenshotJournal/caps/' + val + '.jpg'
os.system(systemString)
print(systemString)



appString ='date >> /Users/Jonah/githubProjects/screenshotJournal/dates.txt'
os.system(appString)


with open('/Users/Jonah/githubProjects/screenshotJournal/int.txt','w') as f:
        f.write(str(intVal+1))
        print("next value: "+str(intVal+1))

