def lesser_og_two_evens(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    elif a%2!=0 or a%2==0:
        print(max(a,b))
    else:
        print(max(a,b))


lesser_og_two_evens(2,4)
lesser_og_two_evens(3,5)
