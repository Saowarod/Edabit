# def find_missing(lst):
#     return [x for x in range(lst[0], lst[-1]+1) 
#                                if x not in lst]
    
# #อิหยังนิ
# lst = [11, 12, 15, 16, 17]
# o = max(lst)
# m = min(lst)
# print("**************************")
# print("Sum of Missing Number")
# print("**************************")
# print("Range of NUmbers")
# print("min = " , m)
# print("max = " , o)
# print("total = ", m + o)
# print("**************************")
# print("Missing NUmbers")
# print(find_missing(lst))
# total = 0
# for n in find_missing(lst):
#     total= total + n  
# print(total)
# print("**************************")

def sum_missing_numbers(lst):
    	return sum(range(min(lst), max(lst) + 1)) - sum(lst)
 
lst = [10, 11, 12, 15, 16, 17]
o = max(lst)
m = min(lst)
print("min = " , m)
print("max = " , o)
print("total = ", m + o)
print("**************************")
print("Missing NUmbers")
print(sum_missing_numbers(lst))
