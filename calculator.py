def calculate():
    #taking input from user for the numbers to calculate
    a= int(input("Enter the first number: "))
    b= int(input("Enter the second number: "))
    print('''1.Addition
    2.Subtraction
    3.Multiplication
    4.Division''')
    #taking the operation as input from the user
    #using loop so that in case user has multiple operation they donot need to start over again
    while True:
        c=(input("Choose the operation(1/2/3/4/stop/restart):"))
        if c=='1':
            print( a,"+",b,"=",a+b)
        elif c=='2':
            print( a,"-",b,"=",a-b)
        elif c=='3':
            print( a,"*",b,"=",a*b)
        elif c=='4':
            print(a,"/",b,"=",a/b)
        elif c=='stop':
            break
        elif c=='restart':
            calculate()
        else:
            print("Error: invalid input.")
            
calculate()
