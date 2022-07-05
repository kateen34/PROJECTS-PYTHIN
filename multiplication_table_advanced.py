#program find the multiplication
#import time module
import time
print('Multiplication Table Maker \n ================')
numb = int(input('enter any integer \n'))

for i in range(1,numb+1):
    print(i," times table \n ===========")
    time.sleep(1)
    for j in range( 1, 13):
        print(i, "X", j, "=", i*j )
