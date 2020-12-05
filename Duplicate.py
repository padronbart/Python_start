i = 0
l = []

def Duplicate(n):
    global i 
    global l
    print(i)
    i += 1
    if n == 1:
        l.append(n)
        return n
    else:
        l.append(n)
        Duplicate(n - 1)
        l.append(n)
        Duplicate(n - 1 )
        print(i)
    return l


if __name__ == "__main__":
    n =  Duplicate(3)
    print(n)
