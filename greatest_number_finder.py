#finding the greatest number
print("greatest number finder\n ===========")

#entering the data
print("enter three number numbers")
first_number=int(input("enter the first number : \n"))
second_number=int (input("enter the second number : \n"))
third_number= int(input("enter the third number : \n"))

# checking for the greatest number
if ( (first_number > second_number) &(first_number> third_number) ):
    print(first_number,"is the greatest number")
elif( (second_number>first_number) & ( second_number >third_number)):
    print(second_number,"is the greatest number")
else:
    print(third_number, "is the greatest number")
