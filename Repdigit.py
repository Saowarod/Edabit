def is_repdigit(num):
    x = list(str(num))
    if num == 0:
        return True
    elif num > 0:
        for n in x:
            if x.count(n) > 1:
                return True
            return False
    return False

num = (66)
print(is_repdigit(num))