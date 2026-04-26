while True:
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Off')
    n = int(input('Enter any one option from above: '))
    num = [1,2,3,4,5]
    # if n in num:
    #     pass
    # else :
    #     print('Please enter valid option')

    # if n in num:
    #     if n==1:
    #         x = int(input('Enter how may number you want to add : '))
    #         sum=0
    #         for i in range(1,x+1):
    #             number = int(input(f'Enter {i} number: '))
    #             sum+=number
    #         print('Addtion is : ',sum)
    # else :
    #     print('Please enter valid option')

    if n in num:
        if n==1:
            x = int(input('Enter how may number you want to add : '))
            l=[]
            sum=0
            for i in range(1,x+1):
                number = eval(input(f'Enter {i} number : '))
                l.append(number)
                sum+=number
            # print('Addtion is : ',sum)
            print(f'Addition of given number {l} is : {sum}')
        elif n==2:
            x = int(input('Enter how may number you want to Subtract : '))
            l=[]
            sub=-(0)
            for i in range(1,x+1):
                number = eval(input(f'Enter {i} number : '))
                l.append(number)
                sub+=number
            # print('Addtion is : ',sum)
            print(f'Subtraction of given number {l} is : {sub}')
        elif n==3:
            x = int(input('Enter how may number you want to multiply : '))
            l=[]
            mul=1
            for i in range(1,x+1):
                number = eval(input(f'Enter {i} number : '))
                l.append(number)
                mul*=number
            # print('Addtion is : ',sum)
            print(f'Multiplication of given number {l} is : {mul}')
        elif n==4:
            x = int(input('Enter how may number you want to divide : '))
            l=[]
            div=[0]
            for i in range(1,x+1):
                number = eval(input(f'Enter {i} number : '))
                l.append(number)
                div/=number
            # print('Addtion is : ',sum)
            print(f'Division of given number {l} is : {div}')
        elif n==5:
            break
    else :
        print('Please enter valid option')