def age_check(age):
    try:
        print(f'your age {age}')
        if age < 18:
            print("you cant drink")
        else:
            print("enjoy your drink")
    except:
        return None


age_check(19)
age_check(14)

y = [10, 20, 30]
try:
    index, x = map(int, input("값을 넣으세요 : ").split())
    print(y[index] / x)
except ZeroDivisionError:
    print("do not input zero(0)")
