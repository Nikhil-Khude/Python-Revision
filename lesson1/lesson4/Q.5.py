a = float(input("enter a first No.="))
b = float(input("enter a second No.="))

for i in range(1,1000):
    if i%a==0 and i % b== 0:
        print("the first number divisible by both :",i)
        break
