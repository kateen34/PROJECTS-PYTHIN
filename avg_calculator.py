#mean average calculator
#asking for number
list=[]
num =0
total =0
median=0
for i in range(5):
    num=int(input("enter any integer : \n"))
    list.append(num)
list.sort()
total=len(list) +1

median = int((total / 2) - 1)
 
print(list,"median:",list[median])
    


    
