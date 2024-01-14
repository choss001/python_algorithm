#foo = 0 # <- ✖
#def outer():
#    foo = 5 # <- ✖
#    def middle():
#        foo = 10 # <- 〇
#        def inner():
#            nonlocal foo # Here
#            foo += 1
#            print(foo) # 11
#        inner()
#    middle()
#outer()


foo = 0 # <- 〇
def outer():
    foo = 5 # <- ✖
    def middle():
        foo = 10 # <- ✖
        def inner():
            global foo # Here
            foo += 1
            print(foo) # 1
        inner()
    middle()
outer()
