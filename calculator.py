def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y    

def div(x,y):
    return x/y    


print("the operation are:")
print("1.add 2.sub 3.mul 4.div") 
selection = input("Enter your operatio")  
number1 = int(input("Enter your first number: ")) 
number1 = int(input("Enter your second number: ")) 

if selection == '1':
    print(number1 , '+' , number2 , '=' , add(number1,number2))
    elif selection == '2':
        print(number1 , '-' , number2 , '=' , sub(number1,number2))
    elif selection == '3' :
        print(number1 , '*' , number2 , '=' mul(number1,number2))   
    elif selection == '4' :
        print(number1 , '/' , number2 , '=' div(number1,number2))   
    else:
        print("invalid input")   