def foo(*args):
    s = sorted(args)
    st = str(s)
    up = st.upper()
    return up

p = foo("snow","glacier","iceberg")
print(p)