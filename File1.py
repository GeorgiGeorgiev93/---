#sum of n numbers
total = 0
n = int(input("Въведете брой числа които ще събираме: "))

for i in range(n):
    try:
        num = int(input(f"Въведете число номер {i+1}: "))
        total += num
    except ValueError:
        print("Въвеждайте само цели числа")

print(f"Общата сума е : {total}")
