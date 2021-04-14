def concat(*args):
    m = []
    for i in [*args]:
        m.extend(i)
    return(m)

args = ([1, 2, 3], [4, 5], [6, 7])
print(concat(*args) , "\n")