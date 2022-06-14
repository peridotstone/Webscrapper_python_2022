def plus(a, b):
    return change(a, b, "+")


def mius(a, b):
    return change(a, b, "-")


def times(a, b):
    return change(a, b, "*")


def division(a, b):
    return change(a, b, "/")


def negation(a):
    if a.isdecimal():
        a = int(a)
        return a * -1
    else:
        return "Please enter a number."


def power(a, b):
    return change(a, b, "**")


def change(a, b, math):
    try:
        a = int(a)
        b = int(b)
        if math is "+":
            return a + b
        elif math == "-":
            return a - b
        elif math == "*":
            return a * b
        elif math == "/":
            return a / b
        elif math == "**":
            return a ** b
    except:
        return "Please enter a number."


print(plus(4, 7))
print(mius("4", 7))
print(times("4", "7"))
print(division("4", "7"))
print(negation("4"))
print(power("4", "7"))
print(plus("a", 4))
print(negation("haha"))
