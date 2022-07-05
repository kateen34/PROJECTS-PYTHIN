#median finder
#mean average calculator
#asking for number
list=[]
median = 0
numb = 0
num1=0
num2 =0
num3=0
n=0
while (numb !=-1):
    numb = int(input("enter any  positve or enter -1 to show result : \n"))
    list.append(numb)
    list.sort()
if ( num1 % 2 ==0):
     n= len(list)
     median1= list[n//2]
     median2= list[n//2 -1]
     median =(median1 +median2)
else:
    median = list[n//2]

print("median is" , median)

    
