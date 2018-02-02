#########calculater Program###############
print("Select 1 For Addition!")
print("Select 2 For Subtraction!")
print("Select 3 For Multiplication!")
print("Select 4 For Division!")
num=int(input("Enter Your Choice"))
number1=int(input("Enter the First Number"))
number2=int(input("Enter the Second Number"))
if num==1:
    number3=number1+number2
    print(number3)
elif num==2:
    number3=number1-number2
    print(number3)
elif num==3:
    number3=number1*number2
    print(number3)
elif num==4:
    number3=number1/number2
    print(number3)
else:
    print("You Enter the Wrong choice")
    
