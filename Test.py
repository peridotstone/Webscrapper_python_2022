def plus(a, b):
    return calculator(a, b, "+")


def calculator(a, b, math):
    try:
        a = int(a)
        b = int(b)
        if math == "+":
            return "{0} + {1}의 결과물은 {2}".format(a, b, a+b)
    except:
        return "please enter a number"


def negation(a):
    if a.isdecimal():
        a = int(a)
        return a*-1
    else:
        return "please enter a number"


print(plus(10, 10))
# print(negation("law"))
# print(negation("10"))
