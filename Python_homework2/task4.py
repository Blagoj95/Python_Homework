def foo(cel):
    if(cel>25):
        return "Hot"
    elif(cel>=15 and cel<=25):
        return "Warm"
    elif(cel<15):
        return "Cold"

temp = foo(14)

print(temp)