def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) 
                               if x not in lst]
#อิหยังนิ
lst = [1, 2, 3, 4, 8]
print(find_missing(lst))
total = 0
for n in find_missing(lst):
    total= total + n
    # print(n)
    
print(total)
