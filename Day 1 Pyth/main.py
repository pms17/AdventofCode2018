freqf=0
freqi=0
freqList=[]


x=0

#dump = open("dump.txt","w")


#Input file handling
freqFile = open("input.txt",'r')
freqString=freqFile.readlines()
freqFile.seek(0)
numLines = sum(1 for line in freqString)

#

for i in range(0,numLines):
    if freqString[i][0]=="+":
        freqf=freqf + int(freqString[i][1:])
    else:
        freqf=freqf - int(freqString[i][1:])
    
    
    


print(freqf)
    
    
    
   




#print(numLines)


freqFile.close()






