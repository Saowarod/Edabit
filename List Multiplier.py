def multiply(lst):
    return [[i]*len(lst) for i in lst]

lst = ["/", "*", "+"]

print(multiply(lst))