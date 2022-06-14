def plus(a,b):
    return calculator(a,b,"+")

def negation(a):
    if a.isdecimal():
        a=int(a)
        return a*-1
    else:
        return "please enter a number"


def calculator(a,b,math):
    try:
        a=int(a)
        b=int(b)
        if math == "+":
            return a+b
        
    except:
        return "please enter a number"
    
print(plus(10,10))
print(negation("law"))
print(negation("10"))


a = chr(54)
print(f'1. chr(54) = {a}, type(a) = {type(a)}')