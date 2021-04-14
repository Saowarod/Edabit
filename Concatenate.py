# def concat(*args):
#     m = []
#     for i in [*args]:
#         m.extend(i)
#     return(m)

# args = ([1, 2, 3], [4, 5], [6, 7])
# print(concat(*args) , "\n")

def concat(*args):
    answer = []
    for arg in args:
        for item in arg:
            answer.append(item)
            
    return answer
	
args = ([1, 2, 3], [4, 5], [6, 7])
print("\n",concat(*args) , "\n")

	
