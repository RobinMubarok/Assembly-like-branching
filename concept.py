def _dan_(a, b, c):
    print(((1%((a+1)+1))*(1%((b+1)+1)))*str(c))
def _atau_(a, b, c):
    print((1%((1%((a+1)+1))+(1%((b+1)+1))))*str(c))
def ine(a, b, c):
    print(bool(abs((1%(abs(a-b)+1)))-1)*(c))
def strint(a):
    return int(''.join(map(str, list(map(ord, list(a))))))
def ice(a, b, c):
    print(bool((abs((1%(abs(strint(a)-strint(b))+1)))-1)*(abs((1%(abs(len(a)-len(b))+1)))-1))*(c))

