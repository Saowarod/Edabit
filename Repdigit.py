# def is_repdigit(num):
#     #x = list(str(num))
#     if num == 0:
#         return True
#     elif num > 0:
#         # for n in x:
#         #     if x.count(n) > 1:
#         #         return True
#             return True
#     return False

# num = int(input("Enter number : "))
# print(is_repdigit(num), "\n")

def repdigit(num):
    for ele in str(num):
        if ele != str(num)[0]:
            return False
            break
        else:
            continue
    return True

num = int(input("Enter number : "))
print(repdigit(num), "\n")