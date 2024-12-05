def create_table(lista):
    a = "CREATE TABLE Pessoas ("
    for x,y in enumerate(lista):
        a+=y
        if x !=len(lista)-1:
            a+=","

    a +=")"
    print(a)

