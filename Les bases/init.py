

#fonction -> 2 saut de ligne apre pour close la ft
def text():
    print("text de ma fonction")


def test_variable():
    a = 10
    tmp = a
    print("val de A : 	", a)
    b = 5
    print("val de B : 	", b)
    c = a + b
    print("val de A + B :  ", c)
    a = b
    b = tmp
    print("Switch A : 	", b)
    print("Switch B : 	", b)
    
    
#exec
if __name__ == '__main__' :
    print("\n")
    print("hello world")
    text()
    print("\n")
    test_variable()
    print("\n")

    