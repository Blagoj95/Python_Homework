st = "Print only the words that start with s in this sentence"

split_string = st.split()


for i in split_string:
    first_letter = i[0:1]
    if(first_letter == "s"):
        print(i)
