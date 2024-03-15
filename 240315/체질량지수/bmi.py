a,b = input().split()

a = int(a)**2
b= int(b) * (100**2)

print(b//a)
if b//a > 25:
    print("Obesity")