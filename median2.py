numb=0
n_num = []
median =0
median1= 0
median=0
while (numb != -1):
    numb= input("enter any integer or -1 to see result : \n")
    n_num.append(numb)

n= len(n_num)
n_num.sort()

print('median is :' , n_num)
