num = 1
row = input("Enter row number ")
iter = 1
m = 3
k = 3
if int(row) - k < 0:
    m = 0
elif int(row) - k == 0:
    m = 1
else:
    m = m * (int(row) - k)

sum = 0
for j in range(int(row) + m):
    if iter == int(row) + m:
        for i in range(int(row)):
            sum += num
            num += 2
    iter += 1
    num += 2
print(sum)
