a,b = input().split()

a = int(a)
b= int(b) ** 100

print(b//a)
if b//a > 25:
    print("Obesity")