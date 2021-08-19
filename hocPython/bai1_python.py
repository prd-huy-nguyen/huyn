# def plus(a,b):
#     return a+b

# print(plus(4,5)) 
# ------------------------------
# check= False
# while True:
#     try:
#         so = int(input("nhap so \n"))
#         check= True
#         break
#     except:
#         print("Dinh dang dau vao khong hop le \n")

# if check:
#     print("so thap phan: %d se co so bat phan la %o \n" %(so, so))
# -------------------------------

while True:
    try:
        so= float(input("Nhap so thuc: \n"))
        lamTron= int(input("Lam tron bao nhieu so: \n"))
        break
    except:
        print("nhap sai \n")

print("{0:.{1}f}".format(so,lamTron))

lamTronRound = round(so, lamTron)
print("so da duoc lamt tron",lamTronRound)