freqf=0
currentFreq=0
freqList=[]
sumList=[]
n=1

#Input file handling
fFile = open("input.txt",'r')
freqList = [int(line) for line in fFile]
numLines = len(freqList)
#

i=0
while True:
    s=set()
    currentFreq += freqList[i]
    if currentFreq in s:
        print("yas", sumList[i])
        break
    else:
        s.add(currentFreq)

    i += 1

    if i == (numLines)*n - 1:
        n = n + 1
        print(n)
        freqList.extend(freqList)

    

    


#freqf=sum(freqList)
#print(freqf)

print(sumList[-1])
    
    
fFile.close()






