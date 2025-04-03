
def factorial(num:int,result:int)->int :
    if num <= 1 :
        return result
    else :
        return factorial(num -1 ,result * num)

print(factorial(0,1))