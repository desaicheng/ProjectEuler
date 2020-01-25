max = 6*(9**5)
ans = 0
for num in range(2,max+1):
    numString = str(num)
    sum = 0
    for j in numString:
        sum += int(j)**5
    if sum == num:
        ans += sum
print(ans)