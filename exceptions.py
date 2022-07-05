num1=int (input ("enter number 1:\n"))
num2=int (input("enter number 2 : \n"))

try:
  num3= num1/num2
except:
    print("you can\'t divide the number by zero")
else:
    print(num3)

